import streamlit as st

st.title("📊 Total Emissions Summary")

st.markdown("This page shows the combined emissions from all categories based on the values you entered.")

# Retrieve stored emissions safely
fuel = st.session_state.get("fuel_emission", 0)
paddy = st.session_state.get("paddy_emission", 0)
livestock = st.session_state.get("livestock_emission", 0)
electricity = st.session_state.get("electricity_emission", 0)
fertilizer = st.session_state.get("fertilizer_emission", 0)

# Calculate total emissions
total = fuel + paddy + livestock + electricity + fertilizer

# Warning if any missing input
if fuel == 0 or paddy == 0 or livestock == 0 or electricity == 0 or fertilizer == 0:
    st.warning("⚠️ Some categories may not have been filled yet. Please check all pages.")

# Display category-wise emissions
st.subheader("📁 Category-wise Emissions (t CO₂eq)")
st.write(f"🚗 **Fossil Fuel & Firewood:** {fuel:.3f}")
st.write(f"🌾 **Paddy Cultivation:** {paddy:.3f}")
st.write(f"🐄 **Livestock:** {livestock:.3f}")
st.write(f"💡 **Electricity Consumption:** {electricity:.3f}")
st.write(f"🧪 **Fertilizer Application:** {fertilizer:.3f}")

st.markdown("---")

# Total emissions
st.subheader(f"✅ **Total Emissions:** {total:.3f} t CO₂eq")
st.success(f"Overall Total: {total:.3f} tonnes of CO₂ equivalent")

# ------------------------------------------------
# DOWNLOAD AS TEXT FILE (works everywhere)
# ------------------------------------------------

report_text = f"""
CARBON FOOTPRINT SUMMARY
-------------------------
Fossil Fuel & Firewood: {fuel:.3f} t CO₂eq
Paddy Cultivation: {paddy:.3f} t CO₂eq
Livestock: {livestock:.3f} t CO₂eq
Electricity Consumption: {electricity:.3f} t CO₂eq
Fertilizer Application: {fertilizer:.3f} t CO₂eq
-------------------------
TOTAL EMISSIONS: {total:.3f} t CO₂eq
"""

st.download_button(
    label="📄 Download Summary (TXT)",
    data=report_text,
    file_name="Carbon_Emissions_Summary.txt",
    mime="text/plain"
)

# ------------------------------------------------
# PRINT BUTTON (USER CAN SAVE AS PDF)
# ------------------------------------------------

st.markdown("""
### 🖨️ Print or Save as PDF  
Click the button below → then choose **Save as PDF** in your browser.
""")

st.markdown("""
<button onclick="window.print()" style="
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
">
🖨️ Print / Save as PDF
</button>
""", unsafe_allow_html=True)
