import streamlit as st

st.title("📊 Total Emissions Summary")

st.markdown("This page shows the combined emissions from all categories based on the values you entered.")

# Retrieve stored emissions safely
fuel = st.session_state.get("fuel_emission", 0)
paddy = st.session_state.get("paddy_emission", 0)
livestock = st.session_state.get("livestock_emission", 0)
electricity = st.session_state.get("electricity_emission", 0)

# Calculate total emissions
total = fuel + paddy + livestock + electricity

# Check if all values are filled
if fuel == 0 or paddy == 0 or livestock == 0 or electricity == 0:
    st.warning("⚠️ Some categories may not have been filled yet. Please check all pages.")

# Display category-wise emissions
st.subheader("📁 Category-wise Emissions (t CO₂eq)")
st.write(f"🚗 **Fossil Fuel & Firewood:** {fuel:.3f}")
st.write(f"🌾 **Paddy Cultivation:** {paddy:.3f}")
st.write(f"🐄 **Livestock:** {livestock:.3f}")
st.write(f"💡 **Electricity Consumption:** {electricity:.3f}")

# Divider
st.markdown("---")

# Total emissions
st.subheader(f"✅ **Total Emissions:** {total:.3f} t CO₂eq")
st.success(f"Overall Total: {total:.3f} tonnes of CO₂ equivalent")
