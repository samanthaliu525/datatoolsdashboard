# app.py

import streamlit as st
import pandas as pd
import numpy as np

# --- Part 1: How to get your data into the app ---
# This is the most important step. We'll load the data from your GitHub
# repository using its "raw" URL.
# The `@st.cache_data` decorator tells Streamlit to run this function
# only once and cache the result, which is great for performance.

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
        # Create a dummy DataFrame that matches the structure for the plotly plot
        data = pd.DataFrame({
            'Country': ['World'] * 10 + ['USA'] * 10,
            'Year': list(range(2000, 2010)) * 2,
            'Emissions': np.random.rand(20) * 100
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
st.dataframe(df.head())

# --- Part 3: Displaying a Pre-rendered PNG Graph ---
# This section shows how to display a static image file (like a PNG)
# that you have uploaded to your GitHub repository.

st.subheader("Static CO₂ Emissions Line Chart")

# Define the raw URL of your PNG file on GitHub.
# You need to get this URL by going to the image on GitHub, clicking 'Raw', and copying the address.
# I've used a placeholder URL here. Replace this with your actual image URL.
CO2_plot_url = 'https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/85d69e7e6c2771f7ea331a477029062ec754d08d/CO2_world.png'
try:
    # Use st.image() to display the image from the URL.
    st.image(CO2_plot_url, caption='World CO₂ Emissions per Year')
except Exception as e:
    st.error(f"Error loading image from GitHub: {e}")
    st.info("Please make sure the image URL is correct.")

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
