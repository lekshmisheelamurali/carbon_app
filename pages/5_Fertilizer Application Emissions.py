import streamlit as st

st.title("🌱 Fertilizer Application Emissions")

st.markdown("""
This page calculates CO₂ emissions from the use of **Lime** and **Urea** fertilizers.  
Emissions are estimated using emission factors and conversion from **CO₂–C → CO₂**.
""")

# Conversion constants
KG_TO_TON = 0.001
CO2_CONVERSION = 44 / 12   # Convert CO₂–C to CO₂

# -----------------------------
# 🌿 LIME APPLICATION
# -----------------------------
st.subheader("🌿 Lime Application")

lime_kg = st.number_input(
    "Enter Lime used (kg):",
    min_value=0.0,
    value=st.session_state.get("lime_kg", 0.0),
    key="lime_kg"
)

if lime_kg > 0:
    lime_ton = lime_kg * KG_TO_TON
    lime_CO2C = lime_ton * 0.12      # Emission factor (tons of Carbon)
    lime_CO2 = lime_CO2C * CO2_CONVERSION

    st.session_state["lime_emission"] = lime_CO2

    st.write(f"Lime CO₂ Emission: **{lime_CO2:.3f} t CO₂**")
else:
    st.session_state["lime_emission"] = 0
    st.info("Enter Lime quantity to calculate emissions.")

# -----------------------------
# 🌾 UREA APPLICATION
# -----------------------------
st.subheader("🌾 Urea Application")

urea_kg = st.number_input(
    "Enter Urea used (kg):",
    min_value=0.0,
    value=st.session_state.get("urea_kg", 0.0),
    key="urea_kg"
)

if urea_kg > 0:
    urea_ton = urea_kg * KG_TO_TON
    urea_CO2C = urea_ton * 0.20      # Emission factor for urea
    urea_CO2 = urea_CO2C * CO2_CONVERSION

    st.session_state["urea_emission"] = urea_CO2

    st.write(f"Urea CO₂ Emission: **{urea_CO2:.3f} t CO₂**")
else:
    st.session_state["urea_emission"] = 0
    st.info("Enter Urea quantity to calculate emissions.")

# -----------------------------
# TOTAL FERTILIZER EMISSIONS
# -----------------------------
total_fert = st.session_state["lime_emission"] + st.session_state["urea_emission"]
st.markdown("---")
st.success(f"📌 **Total Fertilizer Emission: {total_fert:.3f} t CO₂**")

# Save overall fertilizer emissions for Total Emissions page
st.session_state["fertilizer_emission"] = total_fert

