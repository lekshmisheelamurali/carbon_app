import streamlit as st

st.title("📉 Total Carbon Removal Summary")

st.markdown("""
### Equation Reference  
The total carbon removal (ΔC<sub>G</sub>) is calculated based on the IPCC (2006) Equation 2.9:  
**ΔC<sub>G</sub> = A × G<sub>TOTAL</sub> × CF**

Where:  
- ΔC<sub>G</sub> = Annual increase in biomass carbon stocks (tonnes C yr⁻¹)  
- A = Area of land (ha)  
- G<sub>TOTAL</sub> = Mean annual total biomass growth (tonnes d.m. ha⁻¹ yr⁻¹)  
- CF = Carbon fraction of dry matter (tonne C (tonne d.m.)⁻¹)
""", unsafe_allow_html=True)

st.markdown("---")

# Retrieve stored removal values from session state
tree_removal_c = st.session_state.get("tree_removal_c", 0)  # in tonnes C yr⁻¹

# Convert carbon (C) to CO₂ equivalent
tree_removal_co2 = tree_removal_c * (44 / 12)

# Display category-wise removal
st.write(f"🌳 Tree Biomass Carbon Removal (ΔC₍G₎): **{tree_removal_c:.3f} t C yr⁻¹**")

# Separator
st.markdown("---")

# Display total removal
st.subheader(f"✅ Total Carbon Removal (in CO₂ equivalent): **{tree_removal_co2:.3f} t CO₂eq yr⁻¹**")

st.caption("Developed by Lekshmi M S")
