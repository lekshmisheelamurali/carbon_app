

import streamlit as st

# Page title
st.title("🌍 Carbon Footprint Assessment")

# Introduction text
st.markdown("Welcome! Choose a category below to calculate emissions or removals:")

# Emission categories
st.subheader("💨 Emission Categories")
st.page_link("pages/1_Fossil_Fuel_and_Firewood.py", label="🚗 Fossil Fuel and Firewood Emissions")
st.page_link("pages/2_Paddy_Cultivation.py", label="🌾 Paddy Field Emissions")
st.page_link("pages/3_Livestock_Emissions.py", label="🐄 Livestock Emissions")
st.page_link("pages/4_Electricity_Emissions.py", label="💡 Electricity Consumption Emissions")
st.page_link("pages/5_Fertilizer Application Emissions.py", label="🧪 Fertilizer Application Emissions")  # NEW

# Separator
st.markdown("---")

# Carbon removal section
st.subheader("🌿 Carbon Removal")
st.page_link("pages/7_Tree_Biomass_Removal.py", label="🌳 Tree Biomass Carbon Removal")

# Separator
st.markdown("---")

# Overall summary
st.subheader("📊 Overall Summary")
st.page_link("pages/6_Total_Emissions.py", label="📈 View Total Emissions Summary")
st.page_link("pages/8_Total_Removal.py", label="📉 View Total Carbon Removal Summary")

# Footer
st.markdown("---")
st.caption("Developed by Lekshmi M S")
