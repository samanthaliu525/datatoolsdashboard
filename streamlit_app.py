# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

st.subheader("Static World CO₂ Emissions Line Chart")
CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/85d69e7e6c2771f7ea331a477029062ec754d08d/CO2_world.png'
st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')




CO2_visuals_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/main/CO2_visuals.csv"
CO2_visuals = pd.read_csv(CO2_visuals_url)

st.dataframe(CO2_visuals.head())

# Create the Altair line chart
fig_co2 = alt.Chart(CO2_visuals).mark_line().encode(
    x='Year',
    y='Value',
    color=alt.Color('Country', legend=alt.Legend(title="Country")),
    tooltip=['Country', 'Year', 'Value']
).properties(
    title='Country CO₂ Emissions per Year'
)

# Display the Altair chart in Streamlit
st.altair_chart(fig_co2, use_container_width=True)
