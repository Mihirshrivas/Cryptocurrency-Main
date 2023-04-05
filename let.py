import streamlit as st
import yfinance as yf
import pandas as pd
from prophet import Prophet
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

# Define a dictionary of supported cryptocurrencies
crypto_mapping = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD"}

# Define a function to get historical data for a given cryptocurrency
def get_historical_data(symbol_crypto, start_date, end_date):
    data_crypto = yf.Ticker(symbol_crypto)
    crypto_hist = data_crypto.history(start=start_date, end=end_date)
    crypto_hist.reset_index(inplace=True)
    crypto_hist = crypto_hist[["Date", "Close"]]
    crypto_hist.rename(columns={"Date": "ds", "Close": "y"}, inplace=True)
    return crypto_hist

# Define the Streamlit app
def app():
    # Create a Streamlit sidebar with login and signup pages
    st.sidebar.title("Crypto Prediction")
    page = st.sidebar.selectbox(
        "Select a page",
        options=["Login", "Signup", "Dashboard"]
    )

    if page == "Login":
        # Show a login form
        st.write("Login page")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            # TODO: Verify username and password
            st.success("Logged in!")

    elif page == "Signup":
        # Show a signup form
        st.write("Signup page")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")

        if st.button("Signup"):
            if password == confirm_password:
                # TODO: Add user to database
                st.success("Account created!")
            else:
                st.error("Passwords do not match")

    elif page == "Dashboard":
        # Show a dashboard page
        st.write("Dashboard page")
        crypto_option = st.selectbox(
            "Which Crypto do you want to visualize?",
            options=list(crypto_mapping.keys())
        )

        start_date = st.date_input("Start Date", date.today() - relativedelta(months=1))
        end_date = st.date_input("End Date", date.today())

        symbol_crypto = crypto_mapping[crypto_option]
        crypto_hist = get_historical_data(symbol_crypto, start_date, end_date)

        m = Prophet()
        m.fit(crypto_hist)

        future = m.make_future_dataframe(periods=30)
       ## forecast = m.predict(future)

        st.subheader("Forecast")
        st.write(forecast.tail())

        fig = m.plot(forecast)
        st.write(fig)

# Run the Streamlit app
if __name__ == "__main__":
    app()
