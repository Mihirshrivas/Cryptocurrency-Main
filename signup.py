import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Crypto Price Detection", page_icon=":money_with_wings:")

# Create the sign-up form
st.write("# Sign Up")
st.write("Enter your details to get started:")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Validate the form input
if st.button("Sign Up"):
    if len(name.strip()) == 0:
        st.warning("Please enter your name")
    elif len(email.strip()) == 0:
        st.warning("Please enter your email")
    elif len(password.strip()) == 0:
        st.warning("Please enter a password")
    elif password != confirm_password:
        st.warning("Passwords do not match")
    else:
        st.success("You have successfully signed up!")
