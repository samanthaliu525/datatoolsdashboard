import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Climate Dashboard", layout="wide")
st.title("🌍 Climate Dashboard")
st.caption("Individual: World + US • Group: World + China")

# ---------- load data ----------
@st.cache_data
def load():
    world = pd.read_csv("data/world.csv")
    us = pd.read_csv("data/us.csv")
    china = pd.read_csv("data/china.csv")
    # make sure Year is int to avoid decimals
    for df in (world, us, china):
        if "Year" in df.columns:
            df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    return world, us, china

world, us, china = load()

# ---------- UI ----------
tabs = st.tabs(["World", "US", "China", "Comparison"])

with tabs[0]:
    st.subheader("World")
    metric = st.selectbox("Select variable", [c for c in world.columns if c != "Year"])
    fig, ax = plt.subplots()
    ax.plot(world["Year"], world[metric], marker="o")
    ax.set_xlabel("Year"); ax.set_ylabel(metric); ax.set_title(f"World {metric}")
    ax.xaxis.set_major_formatter(lambda x, _: f"{int(x)}")  # no decimals
    st.pyplot(fig)
    st.divider()
    st.caption("Or show a saved plot:")
    st.image("images/world_plot.png", use_container_width=True)

with tabs[1]:
    st.subheader("United States")
    metric_us = st.selectbox("Select variable (US)", [c for c in us.columns if c != "Year"])
    fig, ax = plt.subplots()
    ax.plot(us["Year"], us[metric_us], marker="o", color="tab:red")
    ax.set_xlabel("Year"); ax.set_ylabel(metric_us); ax.set_title(f"US {metric_us}")
    ax.xaxis.set_major_formatter(lambda x, _: f"{int(x)}")
    st.pyplot(fig)
    st.image("images/us_plot.png", use_container_width=True)

with tabs[2]:
    st.subheader("China")
    metric_cn = st.selectbox("Select variable (China)", [c for c in china.columns if c != "Year"])
    fig, ax = plt.subplots()
    ax.plot(china["Year"], china[metric_cn], marker="o", color="tab:green")
    ax.set_xlabel("Year"); ax.set_ylabel(metric_cn); ax.set_title(f"China {metric_cn}")
    ax.xaxis.set_major_formatter(lambda x, _: f"{int(x)}")
    st.pyplot(fig)
    st.image("images/china_plot.png", use_container_width=True)

with tabs[3]:
    st.subheader("Comparison")
    # pick a shared metric name present in all three, or rename columns beforehand
    shared_metric = st.selectbox(
        "Select variable for comparison",
        [c for c in world.columns if c in us.columns and c in china.columns and c != "Year"]
    )
    fig, ax = plt.subplots()
    ax.plot(world["Year"], world[shared_metric], label="World")
    ax.plot(us["Year"], us[shared_metric], label="US")
    ax.plot(china["Year"], china[shared_metric], label="China")
    ax.set_xlabel("Year"); ax.set_ylabel(shared_metric); ax.set_title(f"{shared_metric}: World vs US vs China")
    ax.legend()
    ax.xaxis.set_major_formatter(lambda x, _: f"{int(x)}")
    st.pyplot(fig)

streamlit run app.py
