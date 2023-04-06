import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from config import FRED_API_KEY, QUANDL_API_KEY
import requests
import quandl
import datetime
import os   

# Fetch data from the Blockchain API
def fetch_bitcoin_chart_data(chart):
    url = f"https://api.blockchain.info/charts/{chart}?timespan=all&format=json"
    response = requests.get(url)
    data = response.json()["values"]
    return pd.DataFrame(data)

# Fetch data from FRED API
def fetch_fed_funds_rate():
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    data = response.json()["observations"]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"])
    return df

# Fetch gold price data from Quandl
def fetch_gold_price():
    quandl.ApiConfig.api_key = QUANDL_API_KEY
    data = quandl.get("LBMA/GOLD", start_date="2009-01-01")
    data.reset_index(inplace=True)
    return data

def fetch_sp500_data():
    quandl.ApiConfig.api_key = QUANDL_API_KEY
    data = quandl.get("MULTPL/SP500_REAL_PRICE_MONTH", start_date="2009-01-01")
    data.reset_index(inplace=True)
    return data

@st.cache_data
def get_chart_data():
    market_price = fetch_bitcoin_chart_data("market-price")
    market_price['x'] = market_price['x'].apply(lambda val: datetime.datetime.utcfromtimestamp(val))
    fed_funds_rate = fetch_fed_funds_rate()
    gold_price = fetch_gold_price()
    gold_price = gold_price[["Date", "USD (PM)"]]
    sp500_data = fetch_sp500_data()
    return market_price, fed_funds_rate, gold_price, sp500_data