import streamlit as st
import string
import random

def random_passwrod():

    def passwrod_generator(Length, use_digits, use_special):
        characters = string.ascii_letters
        
        if use_digits:
            characters += string.digits
            
        if use_special:
            characters += string.punctuation
        
        return ''.join(random.choice(characters) for _ in range(Length))

    st.title("password Generator")

    Length = st.slider("password Length", min_value=8, max_value=32, value=12)

    use_digits = st.checkbox("Include Digits")

    use_special = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
        password = passwrod_generator(Length, use_digits, use_special)
        st.write(f"Generated Password: `{password}`")
