""" import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Set page title and favicon
st.set_page_config(page_title="Crypto Price Detection", page_icon=":money_with_wings:")

# Define function to get crypto data
def get_crypto_data(symbol, start, end):
    data = yf.download(symbol, start=start, end=end)
    return data

# Define function to display chart
def display_chart(data, symbol):
    fig = px.line(data, x=data.index, y="Close")
    fig.update_layout(
        title={
            'text': f"{symbol} Price Chart",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Date",
        yaxis_title="Price (USD)"
    )
    st.plotly_chart(fig)

# Define function to display dashboard
def display_dashboard():
    # Set background color and font color
    st.markdown('<style>body{background-color: #f5f5f5; color: #000000;}</style>', unsafe_allow_html=True)

    # Set page header
    st.title("Crypto Price Detection Dashboard")

    # Get user input
    symbol = st.selectbox("Select a crypto", ["BTC-USD", "ETH-USD", "DOGE-USD"])
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")

    # Get crypto data and display chart
    if start_date < end_date:
        data = get_crypto_data(symbol, start_date, end_date)
        display_chart(data, symbol)
    else:
        st.error("Error: End date must be after start date.")

# Display dashboard
display_dashboard()
 """
import yfinance as yf
import streamlit as st
import plotly.express as px

crypto_mapping = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD"}

st.title("Crypto Price Prediction")
crypto_option = st.selectbox(
    "Which Crypto do you want to visualize?", ("Bitcoin", "Ethereum")
)

symbol_crypto = crypto_mapping[crypto_option]
data_crypto = yf.Ticker(symbol_crypto)

value_selector = st.selectbox(
    "Select a value to visualize", ("Open", "High", "Low", "Close", "Volume")
)

start_date = st.date_input("Start Date", value=data_crypto.info["startDate"])
end_date = st.date_input("End Date", value=data_crypto.info["regularMarketPreviousClose"])

if st.button("Generate"):
    crypto_hist = data_crypto.history(start=start_date, end=end_date)
    fig = px.line(crypto_hist, x=crypto_hist.index, y=value_selector, labels={"x": "Date"})
    st.plotly_chart(fig)
