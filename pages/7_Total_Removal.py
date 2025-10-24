import streamlit as st

st.title("📉 Total Carbon Removal Summary")

# Retrieve stored removal values from session state
tree_removal_c = st.session_state.get("tree_removal_c", 0)  # in tonnes C yr⁻¹

# Convert carbon (C) to CO₂ equivalent
tree_removal_co2 = tree_removal_c * (44 / 12)

# Display category-wise removal
st.write(f"🌳 Tree Biomass Carbon Removal: **{tree_removal_c:.3f} t C yr⁻¹**")

# Separator
st.markdown("---")

# Display total removal
st.subheader(f"✅ Total Carbon Removal: **{tree_removal_co2:.3f} t CO₂eq yr⁻¹**")

st.caption("Developed by Lekshmi M S")

