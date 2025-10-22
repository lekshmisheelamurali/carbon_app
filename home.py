import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Carbon Footprint Assessment",
    page_icon="🌍",
    layout="centered"
)

# --------------------------
# Custom CSS for theme
# --------------------------
st.markdown(
    """
    <style>
    /* Page background and font */
    .stApp {
        background-color: #f7f9f7;  /* Light gray/white background */
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title styling */
    .title {
        color: #2E8B57; /* Sea green */
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Subtitle / welcome text */
    .subtitle {
        color: #355E3B; /* Hunter green */
        font-size: 20px;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #3CB371;
        color: white;
        font-size: 20px;
        font-weight: 600;
        border-radius: 15px;
        padding: 10px 20px;
        margin: 10px 0;
        width: 100%;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #2E8B57;  /* Darker green on hover */
        transform: translateY(-2px);
        color: #ffffff;
    }

    /* Footer */
    .footer {
        color: #355E3B;
        font-size: 14px;
        text-align: center;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Page content
# --------------------------
st.markdown('<div class="title">🌍 Carbon Footprint Assessment</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome! Choose a category below to calculate emissions:</div>', unsafe_allow_html=True)

# --------------------------
# Navigation buttons
# --------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🚗 Fossil Fuel and Firewood Emissions"):
        st.experimental_set_query_params(page="1_Fossil_Fuel_and_Firewood")
        st.experimental_rerun()

with col2:
    if st.button("🌾 Paddy Field Emissions"):
        st.experimental_set_query_params(page="2_Paddy_Cultivation")
        st.experimental_rerun()

col3, col4 = st.columns(2)

with col3:
    if st.button("🐄 Livestock Emissions"):
        st.experimental_set_query_params(page="3_Livestock_Emissions")
        st.experimental_rerun()

with col4:
    if st.button("💡 Electricity Consumption Emissions"):
        st.experimental_set_query_params(page="4_Electricity_Emissions")
        st.experimental_rerun()

# Full-width button for Total Emissions
if st.button("📊 View Total Emissions Summary"):
    st.experimental_set_query_params(page="5_Total_Emissions")
    st.experimental_rerun()

# Footer
st.markdown('<div class="footer">Developed by Lekshmi M S</div>', unsafe_allow_html=True)
