# import libraries
import streamlit as st
import pandas as pd
import numpy as np





st.title("Data Tools Dashboard")
st.write(" the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

if st.button('Say Hello'):
    st.write('Hello')
    
st.subheader("Static World CO₂ Emissions Line Chart")
CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/85d69e7e6c2771f7ea331a477029062ec754d08d/CO2_world.png'
st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')

st.subheader("US CO₂ Emissions and Temperature")
CO2_temp_US_scaled_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/e8a9875fd403e4bf1cd400dc73b59b103884e26d/CO2_temp_US_scaled.png'
st.image(CO2_temp_US_scaled_url, caption='World CO₂ Emissions per Year')

