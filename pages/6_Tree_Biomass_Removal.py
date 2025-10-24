import streamlit as st

# Page title
st.title("🌳 Tree Biomass Carbon Removal")

# Description
st.markdown("""
This calculation estimates **annual increase in biomass carbon stocks** (carbon sequestration) 
for **Tropical Moist Deciduous Forest**, based on **IPCC (2006) Guidelines – Equation 2.9**.


ΔCG = A × GTOTAL × CF

Where:  
- **ΔCG** = Annual increase in biomass carbon stocks (tonnes C yr⁻¹)  
- **A** = Area of land (ha)  
- **GTOTAL** = Mean annual total biomass growth (tonnes d.m. ha⁻¹ yr⁻¹)  
- **CF** = Carbon fraction of dry matter (tonne C (tonne d.m.)⁻¹)
""")

st.markdown("---")

# Section: Parameters
st.subheader("🌿 Input Parameters")

# Area input
area = st.number_input("Enter the area (in hectares):", min_value=0.0, step=0.1)

# Above-ground biomass selection
biomass_option = st.radio(
    "Select the Above-ground Biomass Range (tonnes ha⁻¹):",
    ("< 125", "> 125")
)

# Constants for Tropical Moist Deciduous Forest
GW = 8  # above-ground biomass growth (tonnes d.m. ha⁻¹ yr⁻¹)
CF = 0.47  # carbon fraction of dry matter

# Select R value based on biomass range
if biomass_option == "< 125":
    R = 0.20
else:
    R = 0.24

# Compute total biomass growth (GTOTAL)
GTOTAL = GW * (1 + R)

# Compute annual increase in carbon stock
delta_CG = area * GTOTAL * CF

# Display results
st.markdown("---")
st.subheader("📊 Results")

if area > 0:
    st.write(f"**Selected Parameters:**")
    st.write(f"- Above-ground biomass growth (GW): {GW} tonnes d.m. ha⁻¹ yr⁻¹")
    st.write(f"- Below-ground biomass ratio (R): {R}")
    st.write(f"- Carbon fraction (CF): {CF}")
    st.write(f"- Area (A): {area} ha")

    st.markdown("### 🌲 Annual Increase in Biomass Carbon Stocks")
    st.success(f"**ΔCG = {delta_CG:.2f} tonnes C yr⁻¹**")

    st.caption("Calculated using IPCC 2006 Guidelines for Tropical Moist Deciduous Forests (Tier 1).")
else:
    st.info("Please enter a valid area to calculate carbon sequestration.")

# Footer
st.markdown("---")
st.caption("Developed by Lekshmi M S")
