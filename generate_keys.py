import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

names= ["Mihir shrivas", "Bhushan"]
usernames = [" mshrivas","bhupatil"]
passwords = ["abc123", "def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = path(_file_).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)