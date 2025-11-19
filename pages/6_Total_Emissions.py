import streamlit as st
from fpdf import FPDF  # Now this will work!

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

# Warning if missing input
if fuel == 0 or paddy == 0 or livestock == 0 or electricity == 0 or fertilizer == 0:
    st.warning("⚠️ Some categories may not have been filled yet. Please check all pages.")

# Display category-wise emissions
st.subheader("📁 Category-wise Emissions (t CO₂eq)")
st.write(f"🚗 Fossil Fuel & Firewood: {fuel:.3f}")
st.write(f"🌾 Paddy Cultivation: {paddy:.3f}")
st.write(f"🐄 Livestock: {livestock:.3f}")
st.write(f"💡 Electricity Consumption: {electricity:.3f}")
st.write(f"🧪 Fertilizer Application: {fertilizer:.3f}")

st.markdown("---")

# Total emissions
st.subheader(f"✅ Total Emissions: {total:.3f} t CO₂eq")
st.success(f"Overall Total: {total:.3f} tonnes of CO₂ equivalent")

# --------------------------------------------------------------
# PDF GENERATION (REAL PDF DOWNLOAD)
# --------------------------------------------------------------

def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Carbon Footprint Summary", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt=f"Fossil Fuel & Firewood: {fuel:.3f} t CO2eq", ln=True)
    pdf.cell(200, 8, txt=f"Paddy Cultivation: {paddy:.3f} t CO2eq", ln=True)
    pdf.cell(200, 8, txt=f"Livestock: {livestock:.3f} t CO2eq", ln=True)
    pdf.cell(200, 8, txt=f"Electricity Consumption: {electricity:.3f} t CO2eq", ln=True)
    pdf.cell(200, 8, txt=f"Fertilizer Application: {fertilizer:.3f} t CO2eq", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt=f"TOTAL EMISSIONS: {total:.3f} t CO2eq", ln=True)

    return pdf.output(dest="S").encode("latin-1")

pdf_bytes = create_pdf()

st.download_button(
    label="📄 Download PDF Report",
    data=pdf_bytes,
    file_name="Carbon_Emissions_Summary.pdf",
    mime="application/pdf",
)
