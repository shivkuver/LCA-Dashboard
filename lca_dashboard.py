
# AI-Powered LCA Dashboard with Streamlit

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Simulated LCA data
data = pd.DataFrame({
    'Stage': ['Raw Material', 'Processing', 'Assembly', 'Transport', 'Use Phase', 'End-of-Life'],
    'CO2 Emissions (kg)': [120, 200, 150, 180, 300, 100],
    'Water Use (liters)': [500, 700, 450, 400, 600, 200],
    'Energy (kWh)': [1000, 1600, 1200, 900, 2100, 500]
})

# Streamlit UI
st.title("🌿 AI-Powered Life-Cycle Assessment Dashboard")
st.markdown("Simulate environmental impacts across the life cycle of a product using AI-powered controls.")

st.sidebar.header("Simulate Scenario")
material_option = st.sidebar.selectbox("Material Type", ["Virgin", "Recycled"])
transport_mode = st.sidebar.selectbox("Transport Mode", ["Air", "Truck", "Rail", "Ship"])

# Apply interventions
if material_option == "Recycled":
    data.loc[data['Stage'] == "Raw Material", 'CO2 Emissions (kg)'] *= 0.6

if transport_mode == "Rail":
    data.loc[data['Stage'] == "Transport", 'CO2 Emissions (kg)'] *= 0.5
elif transport_mode == "Ship":
    data.loc[data['Stage'] == "Transport", 'CO2 Emissions (kg)'] *= 0.3
elif transport_mode == "Air":
    data.loc[data['Stage'] == "Transport", 'CO2 Emissions (kg)'] *= 1.2

# Charts
st.subheader("📊 CO2 Emissions by Stage")
fig = px.bar(data, x='Stage', y='CO2 Emissions (kg)', color='Stage')
st.plotly_chart(fig)

st.subheader("💧 Water Use Distribution")
fig2 = px.pie(data, names='Stage', values='Water Use (liters)')
st.plotly_chart(fig2)

st.subheader("⚡ Energy Usage Trend")
fig3 = px.line(data, x='Stage', y='Energy (kWh)', markers=True)
st.plotly_chart(fig3)

st.info("Modify options in the sidebar to test different sustainability strategies.")
