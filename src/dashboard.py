import json

import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.title("Chat Metrics Dashboard")

with st.expander("Statistics"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(1000), ax=ax)   
    st.pyplot(fig)