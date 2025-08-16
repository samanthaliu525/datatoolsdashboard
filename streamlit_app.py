# app.py

import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Static World CO₂ Emissions Line Chart")


CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/85d69e7e6c2771f7ea331a477029062ec754d08d/CO2_world.png'
st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')


# --- Part 4: A simple interactive element for a different plot
st.subheader('Bar Chart by Country and Year')
# Let's use a slider to filter by year, assuming the data has a 'Year' column.
# We'll use the unique years from the dataset to set the slider range.
if 'Year' in df.columns:
    # Use float for min/max to avoid issues with mixed types, then cast
    min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
    selected_year = st.slider(
        'Select a year for the bar chart:',
        min_value=min_year,
        max_value=max_year,
        value=max_year
    )

    # Filter the dataframe based on the slider value
    filtered_df_bar = df[df['Year'] == selected_year]

    # Create a new bar chart with the filtered data
    st.bar_chart(filtered_df_bar, x='Country', y='Emissions')
else:
    st.info("Data does not contain a 'Year' column for this example.")
