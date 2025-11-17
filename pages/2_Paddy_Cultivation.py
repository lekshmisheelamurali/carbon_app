import streamlit as st

st.title("🌾 Paddy Field Emissions (CH₄ → CO₂eq)")

# Emission factors
EF_PADDY = 0.011      # kg CH4 / m² / season
CH4_TO_CO2EQ = 28     # GWP (CH4 → CO2eq)

# User inputs with session_state keys
paddy_area_per_season = st.number_input(
    "Enter harvested area per season (m²):",
    min_value=0.0,
    value=st.session_state.get("paddy_area_per_season", 0.0),
    key="paddy_area_per_season"
)

paddy_cycles_per_year = st.number_input(
    "Enter number of cultivation cycles per year:",
    min_value=0,
    value=st.session_state.get("paddy_cycles_per_year", 0),
    key="paddy_cycles_per_year"
)

# Calculation
annual_CH4_kg = EF_PADDY * paddy_area_per_season * paddy_cycles_per_year
annual_CH4_ton = annual_CH4_kg / 1000
annual_CO2eq_paddy = annual_CH4_ton * CH4_TO_CO2EQ

# Save in session state
st.session_state["paddy_emission"] = annual_CO2eq_paddy
st.session_state["paddy_CH4_ton"] = annual_CH4_ton

# Output
st.subheader("Result (t CO₂eq)")
st.write(f"Paddy Field Emission: {annual_CO2eq_paddy:.3f} t CO₂eq")
