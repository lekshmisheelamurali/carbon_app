import streamlit as st

st.title("📊 Total Emissions Summary")

# Retrieve stored emissions from session state
fuel = st.session_state.get("fuel_emission", 0)
paddy = st.session_state.get("paddy_emission", 0)
livestock = st.session_state.get("livestock_emission", 0)
electricity = st.session_state.get("electricity_emission", 0)

# Calculate total emissions
total = fuel + paddy + livestock + electricity

# Display category-wise emissions
st.write(f"🚗 Fossil Fuel & Firewood: **{fuel:.3f} t CO₂eq**")
st.write(f"🌾 Paddy Cultivation: **{paddy:.3f} t CO₂eq**")
st.write(f"🐄 Livestock: **{livestock:.3f} t CO₂eq**")
st.write(f"💡 Electricity Consumption: **{electricity:.3f} t CO₂eq**")

st.markdown("---")
st.subheader(f"✅ Total Emissions: **{total:.3f} t CO₂eq**")
