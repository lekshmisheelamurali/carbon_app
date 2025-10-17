import streamlit as st

# Title
st.title("Carbon Footprint Assessment")

# User Inputs
petrol_litre = st.number_input("Enter petrol consumption (litres):", min_value=0.0, value=0.0)
diesel_litre = st.number_input("Enter diesel consumption (litres):", min_value=0.0, value=0.0)
firewood_kg = st.number_input("Enter firewood consumption (kg):", min_value=0.0, value=0.0)

# Conversion factors
PETROL_L_TO_TJ = 0.0000342  # TJ per litre
DIESEL_L_TO_TJ = 0.0000386  # TJ per litre
FIREWOOD_TON_TO_TJ = 0.015  # TJ per tonne
KG_TO_TONNE = 0.001          # kg to tonne

# Emission factors
EF_PETROL = 69.3  # t CO2 / TJ
EF_DIESEL = 74.1  # t CO2 / TJ
EF_FIREWOOD = 112  # t CO2 / TJ

# Calculations
petrol_tj = petrol_litre * PETROL_L_TO_TJ
diesel_tj = diesel_litre * DIESEL_L_TO_TJ
firewood_tj = firewood_kg * KG_TO_TONNE * FIREWOOD_TON_TO_TJ

petrol_emission = petrol_tj * EF_PETROL
diesel_emission = diesel_tj * EF_DIESEL
firewood_emission = firewood_tj * EF_FIREWOOD

total_emission = petrol_emission + diesel_emission + firewood_emission

# Display results with 3 decimal points
st.subheader("CO₂ Emissions (tonnes)")
st.write(f"Petrol: {petrol_emission:.3f} t CO₂")
st.write(f"Diesel: {diesel_emission:.3f} t CO₂")
st.write(f"Firewood: {firewood_emission:.3f} t CO₂")
st.write(f"**Total Emission: {total_emission:.3f} t CO₂**")
