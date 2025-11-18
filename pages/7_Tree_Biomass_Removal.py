import streamlit as st

# Page title
st.title("🌳 Tree Biomass Carbon Removal")

# Description with correct subscripts
st.markdown(r"""
This calculation estimates **annual increase in biomass carbon stocks** (carbon sequestration) 
for **Tropical Moist Deciduous Forest**, based on **IPCC (2006) Guidelines – Equation 2.9**.



""")

st.markdown("---")

# Section: Parameters
st.subheader("🌿 Input Parameters")

# Area input
area = st.number_input("Enter the area (in hectares):", min_value=0.0, step=0.1)

# Above-ground biomass selection
biomass_option = st.radio(
    "Select the Above-ground Biomass Range (tonnes ha⁻¹):",
    ("< 125", "\> 125")
)

# Constants for Tropical Moist Deciduous Forest
GW = 8       # Above-ground biomass growth (tonnes d.m. ha⁻¹ yr⁻¹)
CF = 0.47    # Carbon fraction of dry matter

# Select R value based on biomass range
if biomass_option == "< 125":
    R = 0.20
else:
    R = 0.24

# Compute total biomass growth G_total
G_total = GW * (1 + R)

# Compute annual increase in carbon stock ΔC_g
delta_Cg = area * G_total * CF

# Convert carbon (C) to CO2 equivalent using 44/12 = 3.667
delta_CO2e = delta_Cg * 3.667

# Display results
st.markdown("---")
st.subheader("📊 Results")

if area > 0:
    st.write("**Selected Parameters:**")
    st.write(f"- Above-ground biomass growth (GW): {GW} tonnes d.m. ha⁻¹ yr⁻¹")
    st.write(f"- Below-ground biomass ratio (R): {R}")
    st.write(f"- Carbon fraction (CF): {CF}")
    st.write(f"- Area (A): {area} ha")

    st.markdown("### 🌲 Annual Increase in Biomass Carbon Stocks")

    # Display ΔC_g with correct subscript
    st.success(f"**ΔC₍g₎ = {delta_Cg:.2f} tonnes C yr⁻¹**")

    st.markdown("### 🌎 CO₂ Equivalent (CO₂e)")

    # Display CO₂e result
    st.success(f"**= {delta_CO2e:.2f} tonnes CO₂e yr⁻¹**")

    st.caption("CO₂e calculated using IPCC conversion factor (1 tonne C = 3.667 tonnes CO₂).")

else:
    st.info("Please enter a valid area to calculate carbon sequestration.")

# Footer
st.markdown("---")
st.caption("Developed by Lekshmi M S")
