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



CO2_visuals_url = "https://raw.githubusercontent.com/samanthaliu525/datatoolsdashboard/main/CO2_visuals.csv"
CO2_visuals = pd.read_csv(CO2_visuals_url)

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
