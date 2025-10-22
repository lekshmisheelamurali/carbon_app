import streamlit as st

st.title("🌍 Carbon Footprint Assessment")

st.markdown("Welcome! Choose a category below to calculate emissions:")

st.page_link("pages/1_Fossil_Fuel_and_Firewood.py", label="🚗 Fossil Fuel and Firewood Emissions")
st.page_link("pages/2_Paddy_Cultivation.py", label="🌾 Paddy Field Emissions")
st.page_link("pages/3_Livestock_Emissions.py", label="🐄 Livestock Emissions")
st.page_link("pages/4_Electricity_Emissions.py", label="💡 Electricity Consumption Emissions")
st.page_link("pages/5_Total_Emissions.py", label="📊 View Total Emissions Summary")


st.markdown("---")
st.caption("Developed by Lekshmi M S")
