import streamlit as st
import subprocess

# Set page title and favicon
st.set_page_config(page_title="Crypto Price Prediction", page_icon=":money_with_wings:")

# Define username and password
USERNAME = "jay"
PASSWORD = "123"

# Create the login form
st.write("# Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Validate login input
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Logged in successfully!")

 
    # Run the app.py file
        subprocess.Popen(["python", "app.py"])

    else:
        st.error("Invalid username or password")  
 


