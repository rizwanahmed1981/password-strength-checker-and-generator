import streamlit as st
import string
import random
from password_generator import *

def passwrord_cheker(password):
        
    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password]) # we used "c" for Character of password we can also use "i" instead of "c"
    lower_case =any([1 if c in string.ascii_lowercase else 0 for c in password]) # we used "c" for Character of password we can also use "i" instead of "c"
    special_characters =any([1 if c in string.punctuation else 0 for c in password]) # we used "c" for Character of password we can also use "i" instead of "c"
    digits =any([1 if c in string.digits else 0 for c in password]) # we used "c" for Character of password we can also use "i" instead of "c"
    # print(string.punctuation)
    # print(upper_case) 

    characters = [upper_case, lower_case, special_characters, digits]

    length = len(password)

    score = 0

    with open('common_password_list.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        st.write(f"<p style='color:red; font-size:20px; text-align:center;'>💥 Password was found in Common Password List. Score 0 / 7  Please try to enter a strong password!</p>", unsafe_allow_html=True)
        

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 24:
        score += 1

    # st.write(f"password length is {str(length)}, adding {str(score)} points")

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1
        
    # st.write(f"password has {str(sum(characters))} diffrent character type, adding {str(sum(characters) - 1)} points")

    if score < 4:
        st.write(f"<p style='font-size:18px; color:red; '>Score: {str(score)} / 7, The password is Quite week!❌ you must use a strong password!</p>",unsafe_allow_html=True)
        suggestion = st.text_input(f"Do you Need Help in Generating Strong Password? ").lower()
        if suggestion == "yes":
            random_passwrod()
        else:
            st.write("Its ok you can Write your own password!😊😊")
    elif score == 4:
        st.write(f"<p style='color:orange; font-size:18px;'>Score: {str(score)} / 7,  The password is ok!⛔ but you need a strong password!</p>", unsafe_allow_html=True)
        suggestion = st.text_input("Do you Need Help in Generating Strong Password? ").lower()
        if suggestion == "yes":
            random_passwrod()
        else:
            st.write("Its ok you can Write your own password!😊😊")
    elif score > 4 and score <= 6:
        st.write(f"<p style='color: #a5ff33; font-size:18px;'>Score: {str(score)} / 7 The password is Decent!👍 but you can add a strong password:</p>", unsafe_allow_html=True)
        suggestion = st.text_input("Do you Need Help in Generating Strong Password? ").lower()
        if suggestion == "yes":
            random_passwrod()
        else:
            st.write("Its ok you can Write your own password!😊😊")
    elif score > 6:
        st.write(f"<p style='color: #0a6d1e; font-size:24px;'>Score: {str(score)} / 7, The password is Strong!🦾 Stay safe...</p>", unsafe_allow_html=True)
