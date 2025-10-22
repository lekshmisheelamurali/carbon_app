import streamlit as st

# Title
st.title("💡 Electricity Consumption Emissions")

st.markdown("""
Estimate **CO₂ emissions** from electricity consumption based on the Indian grid emission factor (0.716 tCO₂/MWh).
""")

# Input
st.header("🔢 Input Data")
electricity_kwh = st.number_input(
    "Enter total electricity consumption (kWh):",
    min_value=0.0,
    value=0.0,
    help="Enter the total electricity consumption in kilowatt-hours (kWh)."
)

# Conversion and emission factor
st.markdown("#### ⚙️ Calculation Details")
st.write("- **1 MWh = 1000 kWh**")
st.write("- **Grid emission factor = 0.716 tCO₂ / MWh**")

# Perform calculation
if electricity_kwh > 0:
    electricity_mwh = electricity_kwh / 1000
    emission_factor = 0.716  # tCO₂ per MWh
    emissions_tonnes = electricity_mwh * emission_factor

    st.success(f"**Estimated Emissions:** {emissions_tonnes:.3f} tonnes of CO₂ equivalent")

    st.markdown(f"""
    **Calculation Formula:**
    \nElectricity (MWh) = Electricity (kWh) / 1000  
    \nCO₂ Emissions (tCO₂) = Electricity (MWh) × 0.716
    """)
else:
    st.info("Please enter electricity consumption to calculate emissions.")
