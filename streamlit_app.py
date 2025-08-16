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




top_emittors_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/main/top_10.csv"
top_emittors = pd.read_csv(top_emittors_url)

st.dataframe(top_emittors.head())

!pip install plotly
import plotly.express as px

fig = px.line(
    top_emittors,
    x="Year",
    y="Emissions",
    color="Country",
    animation_frame="Year",  # This is the magic line that creates the animation
    animation_group="Country",
    title="Country CO₂ Emissions per Year",
    labels={"Value": "Emissions (Metric Tonnes)", "Year": "Year"},
    range_x=[top_emittors['Year'].min(), top_emittors['Year'].max()]
)

# Customize the layout for better readability
fig.update_layout(
    xaxis=dict(autorange=False, range=[min(filtered_df['Year']), max(filtered_df['Year'])]),
    title_font_size=20,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14
)

# Display the animated Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
