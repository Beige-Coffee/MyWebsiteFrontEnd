from processing.data_fetch import get_chart_data
from processing.charts import display_pie_chart, build_bitcoin_summary

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import requests
import quandl
import datetime
import os

def home():

    #st.title("Bitcoin Dashboard")
    st.markdown("<h1 style='text-align: center;margin-bottom:0;'>Bitcoin Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid orange;margin:0;'>", unsafe_allow_html=True)

    url = "http://127.0.0.1:8000/stats"

    data = requests.get(url).json()

    build_bitcoin_summary(data)

    chart_col1, chart_col2 = st.columns([5,5])

    # Display content in the first column
    with chart_col2:
        #st.header("Number of Blocks Mined in Last 5 Days")
        st.markdown("<h2 style='text-align: center;'>Blocks Mined by Pool (Last 5 Days)</h2>", unsafe_allow_html=True)
        url = "https://api.blockchain.info/pools?timespan=5days"

        pool_data = requests.get(url).json()

        display_pie_chart(pool_data)

    with chart_col1:

        market_price, fed_funds_rate, gold_price, sp500_data = get_chart_data()

        # Resample and align data by month
        market_price_monthly = market_price.resample('M', on='x').mean().reset_index()
        fed_funds_rate_monthly = fed_funds_rate.resample('M', on='date').mean().reset_index()
        gold_price = gold_price.resample('M', on='Date').mean().reset_index()
        sp500_data_monthly = sp500_data.resample('M', on='Date').mean().reset_index()

        combined_data = pd.merge_asof(market_price_monthly, fed_funds_rate_monthly, left_on="x", right_on="date", direction="nearest")
        combined_data = combined_data.rename(columns={"x": "Date", "y": "Bitcoin Price (USD)", "value": "Federal Funds Rate (%)"})
        combined_data = pd.merge_asof(combined_data, gold_price, on="Date", direction="nearest")
        combined_data.drop(columns='date', inplace=True)
        combined_data = combined_data.rename(columns={"USD (PM)": "Gold Price (USD)"})
        combined_data = pd.merge_asof(combined_data, sp500_data_monthly, on="Date", direction="nearest")
        combined_data = combined_data.rename(columns={"Value": "S&P 500 Price (USD)"})

        # Add a radio button widget to choose between Bitcoin and Gold
        st.subheader("Choose an asset to compare with the Federal Funds Rate:")
        asset_choice = st.selectbox("Choose an asset to compare with the Federal Funds Rate:", ("Bitcoin", "Gold", "S&P 500"), label_visibility="collapsed")

        # Create a dual-axis line chart based on the user's choice
        if asset_choice == "Bitcoin":
            fig = px.line(combined_data, x="Date", y="Bitcoin Price (USD)", title="Bitcoin Market Price and Federal Funds Rate")
            fig.add_scatter(x=combined_data["Date"], y=combined_data["Federal Funds Rate (%)"], yaxis="y2", mode="lines", name="Federal Funds Rate (%)")
            fig.update_layout(yaxis2=dict(title="Federal Funds Rate (%)", overlaying="y", side="right"))
        elif asset_choice == 'Gold':
            fig = px.line(combined_data, x="Date", y="Gold Price (USD)", title="Gold Price and Federal Funds Rate")
            fig.add_scatter(x=combined_data["Date"], y=combined_data["Federal Funds Rate (%)"], yaxis="y2", mode="lines", name="Federal Funds Rate (%)")
            fig.update_layout(yaxis2=dict(title="Federal Funds Rate (%)", overlaying="y", side="right"))
        else:
            fig = px.line(combined_data, x="Date", y="S&P 500 Price (USD)", title="S&P 500 and Federal Funds Rate")
            fig.add_scatter(x=combined_data["Date"], y=combined_data["Federal Funds Rate (%)"], yaxis="y2", mode="lines", name="Federal Funds Rate (%)")
            fig.update_layout(yaxis2=dict(title="Federal Funds Rate (%)", overlaying="y", side="right"))

        # Display the chart in Streamlit
        st.plotly_chart(fig)
