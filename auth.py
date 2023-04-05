import streamlit as st
from auth0.authentication import GetToken
import yfinance as yf
##from streamlit_lottie import st_lottie

import pandas as pd
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.express as px


domain = 'dev-5anc8h35vza0o3vb.us.auth0.com'
client_id = '0qhX1gE53IovXfGrm0GWU6fvApfwDA0T'
client_secret = 'uUcsBYD5zE8cZKE2t9Lw6KeRZ2NyPsemZOsczgvofOnNUj4TBzV8knj5w-1v-sUs'


if 'profile' not in st.session_state:
    st.session_state.profile = None

if st.session_state.profile is None:
    code = st.experimental_get_query_params().get('code', None)

    if code is not None:
        auth0_token = GetToken(domain, client_id, client_secret)
    #    ## token = auth0_token.login(
    #         client_id=client_id,
    #         client_secret=client_secret,
    #         code=code,
    #         redirect_uri='http://localhost:8501/'
    #     )

       ## st.session_state.profile = token['id_token_payload']

        ##st.write(f'Hello, {st.session_state.profile["name"]}')
        crypto_mapping = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD"}

        st.title("Crypto Price Detection")

        crypto_option = st.sidebar.selectbox(
            "Which Crypto do you want to visualize?", ("Bitcoin", "Ethereum")
        )

        start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(months=1))
        end_date = st.sidebar.date_input("End Date", date.today())

        data_interval = st.sidebar.selectbox(
            "Data Interval",
            (
                "1m",
                "2m",
                "5m",
                "15m",
                "30m",
                "60m",
                "90m",
                "1h",
                "1d",
                "5d",
                "1wk",
                "1mo",
                "3mo",
            ),
        )

        symbol_crypto = crypto_mapping[crypto_option]
        data_crypto = yf.Ticker(symbol_crypto)

        value_selector = st.sidebar.selectbox(
            "Value Selector", ("Open", "High", "Low", "Close", "Volume")
        )

        if st.sidebar.button("Generate"):
            crypto_hist = data_crypto.history(
                start=start_date, end=end_date, interval=data_interval
            )
            fig = px.line(crypto_hist, 
            x=crypto_hist.index, y=value_selector,
            labels={"x": "Date"})
            st.plotly_chart(fig)
    else:
        st.write('Please log in to continue.')
        login_url = f'https://{domain}/authorize?response_type=code&client_id={client_id}&redirect_uri=http%3A%2F%2Flocalhost%3A8501%2F&scope=openid%20profile&audience=https%3A%2F%2F{domain}%2Fuserinfo'
        st.markdown(f'[Login]({login_url})')
else:
    st.write(f'Hello, {st.session_state.profile["name"]}')      