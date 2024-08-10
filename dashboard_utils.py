
from config import settings
import pandas as pd
import requests
import pandas_ta as ta
import plotly.graph_objs as go
import datetime

def get_current_time():
    now = datetime.datetime.now()
    return now

def is_non_farm_payrolls_friday(date):
    first_day_of_month = datetime.date(date.year, date.month, 1)
    first_friday = first_day_of_month + datetime.timedelta(days=(4 - first_day_of_month.weekday() + 7) % 7)
    return date == first_friday

def find_non_farm_payrolls_friday(start_date):
    fridays_count = 0
    current_date = start_date
    
    while True:
        current_friday = current_date + datetime.timedelta((4 - current_date.weekday() + 7) % 7)
        fridays_count += 1
        if is_non_farm_payrolls_friday(current_friday):
            return fridays_count, current_friday
        current_date = current_friday + datetime.timedelta(days=1)

def check_nfp_release():
    today = datetime.date.today()
    upcoming_friday = today + datetime.timedelta((4 - today.weekday() + 7) % 7)
    if is_non_farm_payrolls_friday(upcoming_friday):
        return "This coming Friday is Non-Farm Payrolls by 12:30 pm (CET)"
    else:
        fridays_count, nfp_friday = find_non_farm_payrolls_friday(today)
        return f"Non-Farm Payrolls: {fridays_count - 1} Fridays away!"

# Helper function to format numbers
def format_number(value):
    return f"{value:.4f}"

def format_current_time(now):
    return now.strftime("%B %d, %Y %H:%M:%S")

def plot_candlestick_with_indicators(data, title=None, width=1200, height=800):
    """
    Plots a candlestick chart with additional indicators.

    Parameters:
    - data (pd.DataFrame): DataFrame containing 'open', 'high', 'low', 'close',
                           and indicator columns like 'DCL_20_20', 'DCM_20_20', 'DCU_20_20'.
    - title (str): Title of the chart.
    - width (int): Width of the chart.
    - height (int): Height of the chart.
    """

    # Ensure the necessary columns exist in the DataFrame
    required_columns = ['open', 'high', 'low', 'close', 'DCL_20_20', 'DCM_20_20', 'DCU_20_20']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Create the candlestick trace
    candlestick = go.Candlestick(
        x=data.index,
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name='Candlestick'
    )

    # Create the lines for the indicators
    dcl_trace = go.Scatter(
        x=data.index,
        y=data['DCL_20_20'],
        mode='lines',
        name='DCL_20_20',
        line=dict(color='blue')
    )

    dcm_trace = go.Scatter(
        x=data.index,
        y=data['DCM_20_20'],
        mode='lines',
        name='DCM_20_20',
        line=dict(color='orange')
    )

    dcu_trace = go.Scatter(
        x=data.index,
        y=data['DCU_20_20'],
        mode='lines',
        name='DCU_20_20',
        line=dict(color='green')
    )

    # Combine all the traces into a figure
    fig = go.Figure(data=[candlestick, dcl_trace, dcm_trace, dcu_trace])

    # Customize the layout
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Price',
        width=width,
        height=height,
        xaxis_rangeslider_visible=False  # Remove the range slider for a cleaner view
    )

    # Show the plot
    fig.show()


def prepare_data_and_indicators(ticker):
    data = get_ticker_data(ticker)
    
    donc = ta.donchian(high=data.high, 
                       low=data.low, 
                       lower_length=20, 
                       upper_length=20,)
    
    data_joined = (data
               .join(donc)
               .dropna()
              )
    return data_joined



def get_ticker_data(ticker):

    url = ("https://www.alphavantage.co/query?"
           "function=TIME_SERIES_DAILY&"
           f"symbol={ticker}&"
           # "outputsize=full&"
            "datatype=json&"
           f"apikey={settings.av_api_key}")
   
    resp = requests.get(url)
    response_data = resp.json()
    
    if "Time Series (Daily)" not in response_data.keys():
        raise Exception(f"Invalid API call. The ticker symbol {ticker} is not correct")
    
    data = response_data["Time Series (Daily)"]
    return (pd.DataFrame
            .from_dict(data, orient="index")
            .rename_axis(index='date')
            .rename(columns=lambda col: col.split('. ')[1])
            .sort_index(ascending=True)
            .astype({'open': float, 'high': float, 'low': float, 'close': float})
            .select_dtypes(include=[float]))
