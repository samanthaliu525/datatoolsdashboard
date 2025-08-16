import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Tools Dashboard")
st.write("Explore the relationships between CO2 emissions and other variables")

CO2_clean_url= https://github.com/samanthaliu525/datatoolsdashboard/blob/24e1035eacaff777683cb67e24589a71d24a2c43/CO2_world_clean.csv

st.dataframe(CO2_clean_url)

