import streamlit as st

st.title("🐄 Livestock Emissions (CH₄ → CO₂eq)")

CH4_TO_CO2EQ = 28  # GWP

# Livestock emission factors (kg CH4/animal/year)
livestock_data = {
    "Cattle-indigenous (female), 0-12 months": 9.7,
    "Cattle-indigenous (female), 1-3 years": 15.39,
    "Cattle-indigenous (female), Milking": 35.97,
    "Goat (male), <1 year": 2.83,
    "Goat (male), >1 year": 4.23,
    "Goat (female), >1 year Milking": 4.99,
    "Goat (female), >1 year": 4.93,

    # ✅ Added new categories
    "Kasaragode dwarf (female)": 15.36,
    "Kasaragode dwarf (male)": 16.36,
}

livestock_emissions = 0
livestock_results = {}

st.write("Enter livestock count for each category:")

for animal, ef in livestock_data.items():
    key_name = animal.replace(" ", "_").replace(",", "").replace("-", "_")  # unique key
    
    count = st.number_input(
        f"{animal}:",
        min_value=0,
        value=st.session_state.get(key_name, 0),
        key=key_name
    )
    
    emission_ton = (count * ef) / 1000
    emission_co2eq = emission_ton * CH4_TO_CO2EQ

    livestock_emissions += emission_co2eq
    livestock_results[animal] = emission_co2eq

# Save in session state
st.session_state["livestock_emission"] = livestock_emissions
st.session_state["livestock_details"] = livestock_results

# Output
st.subheader("Results (t CO₂eq)")
for animal, emission in livestock_results.items():
    st.write(f"{animal}: {emission:.3f}")

st.success(f"Total Livestock Emission: {livestock_emissions:.3f} t CO₂eq")
