import streamlit as st
import folium
from streamlit_folium import folium_static

# Set page configuration
st.set_page_config(
    page_title="Erbil Urban Analysis Dashboard",
    page_icon="🏙️",
    layout="wide"
)

# Add title
st.title("Erbil Urban Analysis Dashboard")

# Create a simple map centered on Erbil
ERBIL_COORDS = [36.191111, 44.009167]  # Erbil Citadel coordinates
m = folium.Map(location=ERBIL_COORDS, zoom_start=15)

# Display the map
folium_static(m)
