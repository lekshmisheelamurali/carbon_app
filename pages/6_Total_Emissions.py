import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

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

# ---------------------------------------------------------
# PDF DOWNLOAD SECTION
# ---------------------------------------------------------

def create_pdf(filepath="total_emissions.pdf"):
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Total Emissions Summary")

    y -= 40
    c.setFont("Helvetica", 12)

    data_lines = [
        f"Fossil Fuel & Firewood: {fuel:.3f} t CO₂eq",
        f"Paddy Cultivation: {paddy:.3f} t CO₂eq",
        f"Livestock: {livestock:.3f} t CO₂eq",
        f"Electricity Consumption: {electricity:.3f} t CO₂eq",
        f"Fertilizer Application: {fertilizer:.3f} t CO₂eq",
        "-----------------------------------------------",
        f"Total Emissions: {total:.3f} t CO₂eq"
    ]

    for line in data_lines:
        c.drawString(50, y, line)
        y -= 20

    c.save()


# Button to download PDF
if st.button("📄 Download Summary as PDF"):
    filepath = "total_emissions.pdf"
    create_pdf(filepath)

    with open(filepath, "rb") as pdf_file:
        st.download_button(
            label="⬇️ Click to Download PDF",
            data=pdf_file,
            file_name="Total_Emissions_Summary.pdf",
            mime="application/pdf"
        )

    # Delete after sending (optional)
    if os.path.exists(filepath):
        os.remove(filepath)
