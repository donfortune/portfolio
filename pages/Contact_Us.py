import streamlit as st

st.header('Contact Me')
with st.form(key='form'):
    email = st.text_input('Enter your email address')
    text = st.text_area('Write your message here...')
    button = st.form_submit_button('Submit')
    if button:
        print('Button was pressed')
