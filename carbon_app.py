import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍")

st.title("🌿 Carbon Footprint Calculator")
st.write("Estimate your carbon emissions based on your resource use.")

# Input section
st.header("Enter your data")

electricity = st.number_input("Electricity used (kWh/month)", min_value=0.0, step=0.1)
diesel = st.number_input("Diesel used (litres/month)", min_value=0.0, step=0.1)
lpg = st.number_input("LPG used (kg/month)", min_value=0.0, step=0.1)
fertilizer = st.number_input("Fertilizer used (kg N/month)", min_value=0.0, step=0.1)
livestock = st.number_input("Number of cattle", min_value=0, step=1)

# Emission factors (example: kg CO2e per unit)
ef = {
    "electricity": 0.82,
    "diesel": 2.68,
    "lpg": 3.00,
    "fertilizer": 6.3,   # rough value for N fertilizer (IPCC)
    "livestock": 100.0   # per head/year (approx; you can refine)
}

# Calculate emissions
emissions = {
    "Electricity": electricity * ef["electricity"],
    "Diesel": diesel * ef["diesel"],
    "LPG": lpg * ef["lpg"],
    "Fertilizer": fertilizer * ef["fertilizer"],
    "Livestock": livestock * ef["livestock"] / 12,  # monthly value
}

total_emission = sum(emissions.values())

st.subheader("Results")
st.write(f"**Total Monthly Emission:** {total_emission:.2f} kg CO₂e")

# Show a pie chart
import numpy as np

if np.sum(list(emissions.values())) > 0:
    fig, ax = plt.subplots()
    ax.pie(emissions.values(), labels=emissions.keys(), autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
else:
    st.info("Please enter some values above to generate a pie chart.")


# Option to download results
df = pd.DataFrame(emissions.items(), columns=["Source", "Emission (kg CO2e)"])
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download results as CSV", csv, "carbon_footprint.csv", "text/csv")
