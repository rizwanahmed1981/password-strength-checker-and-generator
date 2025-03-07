import streamlit as st
# import random
import string
from functions import *
from password_generator import *


st.title("Password Strength Cheker")

password = st.text_input("Please enter your Password...: ")

if len(password) >= 8:
    passwrord_cheker(password)
else:
    st.write("Password should be atleast 8 charector long! ")
    suggestion = st.text_input("Do you Need Help in Generating Strong Password: ").lower()

    if suggestion == "yes":
        random_passwrod()
    else:
        st.write("Its ok you can Write your own password!😊😊")