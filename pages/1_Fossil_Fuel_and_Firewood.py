import streamlit as st

st.title("🚗 Fossil Fuel and Firewood Emissions")

# Conversion factors
PETROL_L_TO_TJ = 0.0000342  # TJ per litre
DIESEL_L_TO_TJ = 0.0000386  # TJ per litre
FIREWOOD_TON_TO_TJ = 0.015  # TJ per tonne
KG_TO_TONNE = 0.001         # kg to tonne

# Emission factors
EF_PETROL = 69.3   # t CO2 / TJ
EF_DIESEL = 74.1   # t CO2 / TJ
EF_FIREWOOD = 112  # t CO2 / TJ

# User inputs (with session_state keys)
petrol_litre = st.number_input(
    "Enter petrol consumption (litres):",
    min_value=0.0,
    value=st.session_state.get("petrol_litre", 0.0),
    key="petrol_litre"
)

diesel_litre = st.number_input(
    "Enter diesel consumption (litres):",
    min_value=0.0,
    value=st.session_state.get("diesel_litre", 0.0),
    key="diesel_litre"
)

firewood_kg = st.number_input(
    "Enter firewood consumption (kg):",
    min_value=0.0,
    value=st.session_state.get("firewood_kg", 0.0),
    key="firewood_kg"
)

# Calculations
petrol_tj = petrol_litre * PETROL_L_TO_TJ
diesel_tj = diesel_litre * DIESEL_L_TO_TJ
firewood_tj = firewood_kg * KG_TO_TONNE * FIREWOOD_TON_TO_TJ

petrol_emission = petrol_tj * EF_PETROL
diesel_emission = diesel_tj * EF_DIESEL
firewood_emission = firewood_tj * EF_FIREWOOD

# Save individual emissions
st.session_state["petrol_emission"] = petrol_emission
st.session_state["diesel_emission"] = diesel_emission
st.session_state["firewood_emission"] = firewood_emission

# Results
st.subheader("Results (t CO₂)")
st.write(f"Petrol: {petrol_emission:.3f}")
st.write(f"Diesel: {diesel_emission:.3f}")
st.write(f"Firewood: {firewood_emission:.3f}")

total_fuel = petrol_emission + diesel_emission + firewood_emission
st.success(f"Total Fuel & Firewood Emission: {total_fuel:.3f} t CO₂")

# Save total emission for summary page
st.session_state["fuel_emission"] = total_fuel
