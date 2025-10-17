import streamlit as st

# Title
st.title("Carbon Footprint Assessment")

# ==========================
# Fossil Fuel and Firewood Inputs
# ==========================
st.header("Fossil Fuel and Firewood Emissions")

petrol_litre = st.number_input(
    "Enter petrol consumption (litres):", min_value=0.0, value=0.0
)
diesel_litre = st.number_input(
    "Enter diesel consumption (litres):", min_value=0.0, value=0.0
)
firewood_kg = st.number_input(
    "Enter firewood consumption (kg):", min_value=0.0, value=0.0
)

# Conversion factors
PETROL_L_TO_TJ = 0.0000342  # TJ per litre
DIESEL_L_TO_TJ = 0.0000386  # TJ per litre
FIREWOOD_TON_TO_TJ = 0.015  # TJ per tonne
KG_TO_TONNE = 0.001          # kg to tonne

# Emission factors
EF_PETROL = 69.3  # t CO2 / TJ
EF_DIESEL = 74.1  # t CO2 / TJ
EF_FIREWOOD = 112  # t CO2 / TJ

# Calculations for fuel and firewood
petrol_tj = petrol_litre * PETROL_L_TO_TJ
diesel_tj = diesel_litre * DIESEL_L_TO_TJ
firewood_tj = firewood_kg * KG_TO_TONNE * FIREWOOD_TON_TO_TJ

petrol_emission = petrol_tj * EF_PETROL
diesel_emission = diesel_tj * EF_DIESEL
firewood_emission = firewood_tj * EF_FIREWOOD

# ==========================
# Paddy Cultivation Inputs
# ==========================
st.header("Paddy Field Emissions (CH4 to CO2eq)")

paddy_area_per_season = st.number_input(
    "Enter harvested area per season (m²):", min_value=0.0, value=0.0
)
period_days = st.number_input(
    "Enter period of cultivation (days):", min_value=0, value=0
)
paddy_cycles_per_year = st.number_input(
    "Enter number of paddy cultivation cycles per year:", min_value=0, value=0
)

# Paddy emission factor
EF_PADDY = 0.011  # kg CH4 / m² / season
CH4_TO_CO2EQ = 28  # Global warming potential of CH4

# Calculations for paddy
annual_CH4_kg = EF_PADDY * paddy_area_per_season * paddy_cycles_per_year
annual_CH4_ton = annual_CH4_kg / 1000
annual_CO2eq_paddy = annual_CH4_ton * CH4_TO_CO2EQ

# ==========================
# Livestock Inputs
# ==========================
st.header("Livestock Emissions (CH4 to CO2eq)")

# Livestock types and enteric emissions (kg CH4/head/year)
livestock_data = {
    "Cattle-indigenous (female), 0-12 months": 9.7,
    "Cattle-indigenous (female), 1-3 years": 15.39,
    "Cattle-indigenous (female), Milking": 35.97,
    "Goat (male), <1 year": 2.83,
    "Goat (male), >1 year": 4.23,
    "Goat (female), >1 year Milking": 4.99,
    "Goat (female), >1 year": 4.93
}

# Let user select livestock types
selected_livestock = st.multiselect(
    "Select the types of livestock you have:", list(livestock_data.keys())
)

livestock_emissions = 0
livestock_results = {}

# Input number of heads for selected livestock
for animal in selected_livestock:
    ef = livestock_data[animal]
    count = st.number_input(f"Number of {animal}:", min_value=0, value=0)
    emission_ton = (count * ef) / 1000  # kg → tonnes
    emission_co2eq = emission_ton * CH4_TO_CO2EQ
    livestock_emissions += emission_co2eq
    livestock_results[animal] = emission_co2eq

# ==========================
# Total Emission
# ==========================
total_emission = petrol_emission + diesel_emission + firewood_emission + annual_CO2eq_paddy + livestock_emissions

# ==========================
# Display Results
# ==========================
st.subheader("CO₂ Emissions (tonnes)")

st.write(f"Petrol: {petrol_emission:.3f} t CO₂")
st.write(f"Diesel: {diesel_emission:.3f} t CO₂")
st.write(f"Firewood: {firewood_emission:.3f} t CO₂")
st.write(f"Paddy Cultivation: {annual_CO2eq_paddy:.3f} t CO₂eq")

st.subheader("Livestock Emissions (CO2eq t)")
for animal, emission in livestock_results.items():
    st.write(f"{animal}: {emission:.3f} t CO₂eq")

st.write(f"**Total Livestock Emission: {livestock_emissions:.3f} t CO₂eq**")

st.write(f"**Total Emission (All Sources): {total_emission:.3f} t CO₂eq**")
