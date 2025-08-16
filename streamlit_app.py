import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between CO2 emissions and other variables")

CO2_long = pd.Dataframe("CO2_long")

st.dataframe(CO2_long)
