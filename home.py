import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Carbon Footprint Assessment",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS for green-themed buttons and background
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background-color: #e6f2e6;
    }
    
    /* Title style */
    .title {
        color: #1a521a;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
    }

    /* Card-like buttons */
    .card-link {
        display: block;
        padding: 15px;
        margin: 10px 0;
        background-color: #66b266;
        color: white;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        border-radius: 12px;
        transition: 0.3s;
    }
    .card-link:hover {
        background-color: #4d994d;
        color: #f2f2f2;
    }

    /* Footer style */
    .footer {
        color: #1a521a;
        font-size: 14px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<div class="title">🌍 Carbon Footprint Assessment</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:20px; color:#1a521a;'>Welcome! Choose a category below to calculate emissions:</p>", unsafe_allow_html=True)

# Green themed links as card buttons
st.markdown('<a class="card-link" href="pages/1_Fossil_Fuel_and_Firewood.py">🚗 Fossil Fuel and Firewood Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/2_Paddy_Cultivation.py">🌾 Paddy Field Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/3_Livestock_Emissions.py">🐄 Livestock Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/4_Electricity_Emissions.py">💡 Electricity Consumption Emissions</a>', unsafe_allow_html=True)
st.markdown('<a class="card-link" href="pages/5_Total_Emissions.py">📊 View Total Emissions Summary</a>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed by Lekshmi M S</div>', unsafe_allow_html=True)
