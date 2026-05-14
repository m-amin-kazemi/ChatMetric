import json

import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Banner
st.image('./data/banner.png', width=500)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric(label="Bale Group Members", value="3,234", delta="+5%")
col2.metric(label="Rubica Group Members", value="4,567", delta="+1%")
col3.metric(label="Telegram Group Members", value="10,296", delta="+2%")

st.title("📊 Chat Metrics")

# Login/Signup
login_option = st.sidebar.radio('Login/Signup', ['Login', 'Signup'])
if login_option == 'Login':
    with st.sidebar.form("login"):
        st.write("Login to access your dashboard")
        username = st.text_input("Enter your username: ")
        password =st.text_input("Enter your password: ", type="password")

        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("signup"):
        st.write("Signup to create an account")
        username = st.text_input("Choose a username: ")
        email = st.text_input("Enter your email: ")
        password = st.text_input("Choose a password: ", type="password")

        submitted = st.form_submit_button("Signup")
        if submitted:
            pass

# Statistics
with st.expander("Statistics"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(1000), ax=ax)   
    st.pyplot(fig)

# User Profile
with st.expander("User Profile:"):
    col1, col2 = st.columns(2)
    col1.text_input("Name: ")
    col2.text_input("Email: ")
    st.camera_input("Camera Input, key='camera_input'")