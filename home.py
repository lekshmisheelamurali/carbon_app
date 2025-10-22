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
    /* Background and main font */
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

    /* Card buttons for pages */
    .card-link {
        display: block;
        padding: 18px;
        margin: 12px 0;
        background-color: #3CB371; /* Medium sea green */
        color: white;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        text-decoration: none;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: 0.3s;
    }

    .card-link:hover {
        background-color: #2E8B57; /* Darker green on hover */
        color: #ffffff;
        transform: translateY(-2px);
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

# Green-themed card links
st.markdown('<a class="card-link" href="pages/1_Fossil_Fuel_and_Firewood.py">🚗 Fossil Fuel and Firewood Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/2_Paddy_Cultivation.py">🌾 Paddy Field Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/3_Livestock_Emissions.py">🐄 Livestock Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/4_Electricity_Emissions.py">💡 Electricity Consumption Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/5_Total_Emissions.py">📊 View Total Emissions Summary</a>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed by Lekshmi M S</div>', unsafe_allow_html=True)
