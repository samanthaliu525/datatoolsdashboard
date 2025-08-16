# app.py

import streamlit as st
import pandas as pd
import numpy as np

# --- Part 1: How to get your data into the app ---
# This is the most important step. You can load data from various sources.
# In this updated version, we're showing how to load a CSV file directly from a public
# GitHub repository using its "raw" URL.
# The `@st.cache_data` decorator tells Streamlit to run this function
# only once and cache the result, which is great for performance.

# This is the corrected URL for the raw CSV data.
CO2_clean_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/24e1035eacaff777683cb67e24589a71d24a2c43/CO2_world_clean.csv'


@st.cache_data
def load_data():
    """
    Loads the data from a CSV file hosted on GitHub.
    """
    try:
        # pd.read_csv() is used to read the data from the URL and return a DataFrame.
        data = pd.read_csv(CO2_clean_url)
        return data
    except Exception as e:
        st.error(f"Error loading data from GitHub: {e}")
        st.info("Creating a simple dataframe for demonstration purposes.")
        data = pd.DataFrame({
            'Country': ['USA', 'China', 'India', 'Russia'],
            'CO2_Emissions': [15, 20, 10, 12],
            'Year': [2020, 2020, 2020, 2020]
        })
        return data


# Load the data
df = load_data()


# --- Part 2: Building the Streamlit Dashboard UI ---

# Add a title and an introductory header
st.title('CO2 Emissions Dashboard')
st.header('Data Visualization from a Loaded Dataset')

# Display the raw data as a table
st.subheader('Raw Data')
# This is the correct way to display a DataFrame in Streamlit.
st.dataframe(df)

# --- Part 3: Creating Plots with Streamlit's built-in functions ---
# Streamlit has simple functions for common plots. They are fast and easy to use.
# You can also use other libraries like Altair, Plotly, or Matplotlib for more complex plots.

# Bar Chart (assuming 'Country' and 'CO2_Emissions' columns exist)
st.subheader('CO2 Emissions by Country')
st.bar_chart(df, x='Country', y='CO2_Emissions')

# Line Chart (assuming 'Year' and 'CO2_Emissions' columns exist)
st.subheader('Emissions over Time')
# Filter for a specific country for a cleaner line chart example
df_usa = df[df['Country'] == 'USA']
st.line_chart(df_usa, x='Year', y='CO2_Emissions')


# --- Part 4: Adding a simple interactive element ---
# A key feature of Streamlit is its ability to add interactive widgets.
# Let's add a slider to filter the data.

st.subheader('Interactive Plot')
# Let's use a slider to filter by year, assuming the data has a 'Year' column.
# We'll use the unique years from the dataset to set the slider range.
if 'Year' in df.columns:
    min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
    selected_year = st.slider(
        'Select a year:',
        min_value=min_year,
        max_value=max_year,
        value=max_year
    )

    # Filter the dataframe based on the slider value
    filtered_df = df[df['Year'] == selected_year]

    # Create a new bar chart with the filtered data
    st.bar_chart(filtered_df, x='Country', y='CO2_Emissions')
else:
    st.info("Data does not contain a 'Year' column for this example.")

