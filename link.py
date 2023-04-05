import streamlit as st


# Set page title and favicon
st.set_page_config(page_title="Crypto Price Prediction", page_icon=":money_with_wings:")

# Define username and password
USERNAME = "jay"
PASSWORD = "123"

# Create the login form
def login():
    st.write("# Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password")
            return False
        
    st.write("Don't have an account? Click the link below to sign up.")
    if st.button("Sign up"):
        st.experimental_rerun()  # Rerun the app to show the sign-up page

# Create the sign-up form
def signup():
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
            return True

    st.write("Already have an account? Click the link below to log in.")
    if st.button("Log in"):
        st.experimental_rerun()  # Rerun the app to show the login page

    return False

# Main app
def app():
    page = st.sidebar.selectbox("Select a page", ["Login", "Sign Up"])

    if page == "Login":
        if login():
            # Show main app content here
            st.write("Welcome to the Crypto Price Prediction app!")
    else:
        if signup():
            # Show main app content here
            st.write("Welcome to the Crypto Price Prediction app!")

if __name__ == "__main__":
    app()
