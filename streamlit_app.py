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


@st.cache_data
def aggregate_data(df):
    """
    Aggregates the data to show total emissions per year.
    This mimics the functionality of your 'CO2_visuals_sum' DataFrame.
    """
    # Sum up the 'Emissions' for each 'Year'.
    # For this example, we'll assume the loaded data has 'Country' and 'CO2_Emissions'.
    # We will create a new 'Emissions' column for clarity and sum by 'Year'.
    df['Emissions'] = df['CO2_Emissions'].astype(float)
    df_agg = df.groupby('Year')['Emissions'].sum().reset_index()
    df_agg['Country'] = 'World'
    return df_agg


# Load the data
df = load_data()
df_aggregated = aggregate_data(df)


# --- Part 2: Building the Streamlit Dashboard UI ---

# Add a title and an introductory header
st.title('CO2 Emissions Dashboard')
st.header('Interactive Data Visualization with Plotly')

# Display the raw data as a table
st.subheader('Raw Data')
# This is the correct way to display a DataFrame in Streamlit.
st.dataframe(df.head())

# --- Part 3: Creating an Interactive Plot with Plotly ---
# This section converts your lets_plot chart to a fully interactive Plotly chart.
# We'll also add a widget so you can filter by country.

st.subheader("Interactive CO₂ Emissions Line Chart")

# Create a list of unique countries, and add 'World' to the top
countries = sorted(df['Country'].unique().tolist())
countries.insert(0, 'World')

# Create a selectbox for the user to choose a country
selected_country = st.selectbox(
    'Select a Country to view emissions:',
    options=countries
)

# Filter the data based on the user's selection
if selected_country == 'World':
    filtered_df = df_aggregated
else:
    filtered_df = df[df['Country'] == selected_country]

# Now, create the Plotly express line chart with the filtered data
fig = px.line(
    filtered_df,
    x="Year",
    y="Emissions",
    title=f"CO₂ Emissions for {selected_country} over Time",
    labels={"Emissions": "Emissions (Metric Tonnes)", "Year": "Year"},
)

# Customize the chart layout to match the lets_plot style
fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14,
)

# Display the interactive Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

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
