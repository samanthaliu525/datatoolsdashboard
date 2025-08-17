# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt




st.title("Data Tools Dashboard")
st.write("Explore the relationships between and progression of CO₂ Emissions, temperature, GDP per capita, energy use, and number of natural disasters")

if st.button('Say Hello'):
    st.write('Hello')
    
st.subheader("Static World CO₂ Emissions Line Chart")
CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/85d69e7e6c2771f7ea331a477029062ec754d08d/CO2_world.png'
st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')

st.subheader("US CO₂ Emissions and Temperature")
CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/e8a9875fd403e4bf1cd400dc73b59b103884e26d/CO2_temp_US_scaled.png'
st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')

top_emittors_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/main/top_10.csv"
top_emittors = pd.read_csv(top_emittors_url)
top_emittors['Emissions'] = pd.to_numeric(top_emittors['Emissions'].str.replace(',', ''), errors='coerce')
top_emittors['Year'] = pd.to_numeric(top_emittors['Year'], errors='coerce')

st.title('Top 10 CO₂ Emissions Dashboard')
st.header('Interactive Line Chart with Animation')

# Display the raw data for debugging purposes
st.subheader("Raw Data from CSV")
st.dataframe(top_emittors.head())

# --- Part 3: Creating an Interactive Animated Plotly Chart ---
# Use Plotly Express to create the animated line chart.
# The `animation_frame` parameter is what creates the "play button" and slider.
# The `animation_group` parameter keeps the lines connected as the years progress.

st.subheader("Animated Emissions by Country")

if st.button('Say Hello'):
    st.write('Hello')
    
import plotly.express as px

fig = px.line(
    top_emittors,
    x="Year",
    y="Emissions",
    color="Country",
    animation_frame="Year",  # This is the magic line that creates the animation
    animation_group="Country",
    title="Country CO₂ Emissions per Year",
    labels={"Emissions": "Emissions (Metric Tonnes)", "Year": "Year"},
    range_x=[top_emittors['Year'].min(), top_emittors['Year'].max()]
)

# Customize the layout for better readability
fig.update_layout(
    xaxis=dict(autorange=False, range=[min(top_emittors['Year']), max(top_emittors['Year'])]),
    title_font_size=20,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14
)

# Display the animated Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.subheader("Animated Emissions by Country")


st.subheader("Emissions by Country")



CO2_temp_US_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/d3f902e6facd88596ae1367741663ba914119887/CO2_temp_US_scaled.png"
CO2_temp_US_facet_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/d3f902e6facd88596ae1367741663ba9119887/CO2_temp_US_facet.png"
CO2_temp_China_scaled_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/37b578aaecd79f967b66478f6a56ffe878e217ee/CO2_temp_China_scaled.png"




if st.button('United States'):
    st.write("United")
    
    st.image(CO2_temp_US_scaled_url)

if st.button('China'):
    st.image(CO2_temp_China_scaled_url)
    
# Create buttons to choose the plot to display
col1, col2 = st.columns(2)
with col1:
    show_us = st.button("United States")
with col2:
    show_china = st.button("China")

# Use a state variable to track which button was clicked last
if 'last_clicked' not in st.session_state:
    st.session_state.last_clicked = 'us'

if show_us:
    st.session_state.last_clicked = 'us'
elif show_china:
    st.session_state.last_clicked = 'china'

# Display the correct image based on the last clicked button
if st.session_state.last_clicked == 'us':
    st.image(CO2_temp_US_scaled_url, caption="United States")
elif st.session_state.last_clicked == 'china':
    st.image(CO2_temp_China_scaled_url, caption="China")
else: # A default plot if no button has been clicked yet.
    st.image(CO2_temp_US_scaled_url, caption="United States")
