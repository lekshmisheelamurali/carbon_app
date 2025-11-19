import streamlit as st
from fpdf import FPDF

st.title("📊 Total Emissions Summary")

st.markdown("This page shows the combined emissions from all categories based on the values you entered.")

# Retrieve stored emissions safely
fuel = st.session_state.get("fuel_emission", 0)
paddy = st.session_state.get("paddy_emission", 0)
livestock = st.session_state.get("livestock_emission", 0)
electricity = st.session_state.get("electricity_emission", 0)
fertilizer = st.session_state.get("fertilizer_emission", 0)  # NEW

# Calculate total emissions
total = fuel + paddy + livestock + electricity + fertilizer

# Check if all values are filled
if fuel == 0 or paddy == 0 or livestock == 0 or electricity == 0 or fertilizer == 0:
    st.warning("⚠️ Some categories may not have been filled yet. Please check all pages.")

# Display category-wise emissions
st.subheader("📁 Category-wise Emissions (t CO₂eq)")
st.write(f"🚗 **Fossil Fuel & Firewood:** {fuel:.3f}")
st.write(f"🌾 **Paddy Cultivation:** {paddy:.3f}")
st.write(f"🐄 **Livestock:** {livestock:.3f}")
st.write(f"💡 **Electricity Consumption:** {electricity:.3f}")
st.write(f"🧪 **Fertilizer Application:** {fertilizer:.3f}")

# Divider
st.markdown("---")

# Total emissions
st.subheader(f"✅ **Total Emissions:** {total:.3f} t CO₂eq")
st.success(f"Overall Total: {total:.3f} tonnes of CO₂ equivalent")

st.markdown("---")
st.subheader("⬇️ Download or Print Summary")

# -------------------------------------------------
# PDF GENERATION FUNCTION (fpdf2 compatible)
# -------------------------------------------------
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Total Emissions Summary", ln=True, align="C")

    pdf.ln(8)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Fossil Fuel & Firewood: {fuel:.3f} t CO2eq", ln=True)
    pdf.cell(0, 10, f"Paddy Cultivation: {paddy:.3f} t CO2eq", ln=True)
    pdf.cell(0, 10, f"Livestock: {livestock:.3f} t CO2eq", ln=True)
    pdf.cell(0, 10, f"Electricity Consumption: {electricity:.3f} t CO2eq", ln=True)
    pdf.cell(0, 10, f"Fertilizer Application: {fertilizer:.3f} t CO2eq", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"TOTAL: {total:.3f} t CO2eq", ln=True)

    # Convert PDF output to bytes (VERY IMPORTANT)
    pdf_str = pdf.output(dest="S")
    return pdf_str.encode("latin-1")

# Create PDF bytes
pdf_bytes = create_pdf()

# -------------------------------------------------
# STREAMLIT DOWNLOAD BUTTON
# -------------------------------------------------
st.download_button(
    label="📄 Download Summary as PDF",
    data=pdf_bytes,
    file_name="total_emissions_summary.pdf",
    mime="application/pdf"
)

# -------------------------------------------------
# PRINT BUTTON (opens browser print dialog)
# -------------------------------------------------
st.markdown(
    """
    <br>
    <button onclick="window.print()" style="
        background-color:#4CAF50;
        color:white;
        padding:10px 20px;
        border:none;
        border-radius:5px;
        font-size:16px;
        cursor:pointer;">
        🖨️ Print This Page
    </button>
    """,
    unsafe_allow_html=True
)
