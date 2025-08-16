import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between CO2 emissions and other variables")

CO2_clean_url= CO2_world_clean.csv

st.dataframe(CO2_clean_url)

