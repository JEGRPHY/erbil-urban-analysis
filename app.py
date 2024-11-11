import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
import random  # For generating sample data

# Set page configuration
st.set_page_config(
    page_title="Erbil Urban Analysis Dashboard",
    page_icon="🏙️",
    layout="wide"
)

# Add title and description
st.title("Erbil Urban Analysis Dashboard Created By JEGR PHY")
st.markdown("""
This interactive dashboard visualizes various urban features in central Erbil.
Use the sidebar controls to explore different layers and data.
""")

# Sidebar
st.sidebar.title("Map Controls")

# Layer controls with more options
show_landuse = st.sidebar.checkbox("Show Land Use", True)
show_climate = st.sidebar.checkbox("Show Climate Data", False)
show_vegetation = st.sidebar.checkbox("Show Vegetation", False)
show_roads = st.sidebar.checkbox("Show Roads", True)
show_density = st.sidebar.checkbox("Show Population Density", False)

# Additional filters in sidebar
st.sidebar.subheader("Filters")
selected_year = st.sidebar.slider("Select Year", 2015, 2024, 2024)
landuse_types = st.sidebar.multiselect(
    "Land Use Types",
    ["Commercial", "Residential", "Industrial", "Green Space"],
    ["Commercial", "Residential"]
)

# Main layout
col1, col2 = st.columns([3, 1])

# Main map
with col1:
    # Create base map
    ERBIL_COORDS = [36.191111, 44.009167]
    m = folium.Map(location=ERBIL_COORDS, zoom_start=15)

    # Add Citadel marker
    folium.Marker(
        ERBIL_COORDS,
        popup="Erbil Citadel",
        tooltip="Erbil Citadel",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

    # Land Use Layer
    if show_landuse:
        # Sample land use areas
        land_use_areas = {
            "Commercial": {
                "coords": [36.191111, 44.009167],
                "radius": 200,
                "color": "red"
            },
            "Residential": {
                "coords": [36.192111, 44.010167],
                "radius": 300,
                "color": "blue"
            },
            "Industrial": {
                "coords": [36.189111, 44.007167],
                "radius": 250,
                "color": "purple"
            },
            "Green Space": {
                "coords": [36.190111, 44.011167],
                "radius": 150,
                "color": "green"
            }
        }

        for use_type, data in land_use_areas.items():
            if use_type in landuse_types:
                folium.Circle(
                    data["coords"],
                    radius=data["radius"],
                    popup=use_type,
                    color=data["color"],
                    fill=True,
                    fillColor=data["color"],
                    fillOpacity=0.2
                ).add_to(m)

    # Climate Data Layer
    if show_climate:
        # Sample temperature heatmap data
        temp_data = []
        for i in range(20):
            lat = ERBIL_COORDS[0] + random.uniform(-0.003, 0.003)
            lon = ERBIL_COORDS[1] + random.uniform(-0.003, 0.003)
            temp = random.uniform(25, 35)  # Sample temperature values
            temp_data.append([lat, lon, temp])
        
        HeatMap(temp_data).add_to(m)

    # Vegetation Layer
    if show_vegetation:
        vegetation_areas = [
            {"coords": [36.190511, 44.008167], "size": 100, "type": "Dense"},
            {"coords": [36.191711, 44.010167], "size": 150, "type": "Moderate"},
            {"coords": [36.189911, 44.009167], "size": 80, "type": "Sparse"}
        ]

        for area in vegetation_areas:
            folium.Circle(
                area["coords"],
                radius=area["size"],
                popup=f"Vegetation: {area['type']}",
                color="green",
                fill=True,
                fillColor="green",
                fillOpacity=0.3
            ).add_to(m)

    # Roads Layer
    if show_roads:
        roads_data = [
            {
                "coords": [[36.191111, 44.007167], [36.191111, 44.011167]],
                "type": "Main Road",
                "color": "blue",
                "weight": 3
            },
            {
                "coords": [[36.189111, 44.009167], [36.193111, 44.009167]],
                "type": "Secondary Road",
                "color": "orange",
                "weight": 2
            }
        ]

        for road in roads_data:
            folium.PolyLine(
                road["coords"],
                color=road["color"],
                weight=road["weight"],
                popup=road["type"]
            ).add_to(m)

    # Population Density Layer
    if show_density:
        density_data = []
        for i in range(30):
            lat = ERBIL_COORDS[0] + random.uniform(-0.003, 0.003)
            lon = ERBIL_COORDS[1] + random.uniform(-0.003, 0.003)
            weight = random.uniform(0.2, 1.0)
            density_data.append([lat, lon, weight])
        
        HeatMap(
            density_data,
            gradient={0.2: 'blue', 0.5: 'lime', 0.8: 'red'},
            min_opacity=0.3
        ).add_to(m)

    # Display the map
    folium_static(m)

# Information Panel
with col2:
    st.subheader("Area Information")
    st.write("""
    **Central Erbil Statistics:**
    - Area: ~2 km²
    - Major Landmark: Erbil Citadel
    - UNESCO World Heritage Site
    """)
    
    # Add dynamic statistics based on selected layers
    if show_landuse:
        st.subheader("Land Use Distribution")
        st.write(f"Showing {len(landuse_types)} land use types")
        for type in landuse_types:
            st.write(f"- {type}")
    
    if show_climate:
        st.subheader("Climate Information")
        st.write("Temperature Range: 25°C - 35°C")
        st.write("Climate Zone: BSh (Hot semi-arid)")
    
    if show_vegetation:
        st.subheader("Vegetation Coverage")
        st.write("Total Green Areas: 3")
        st.write("- Dense Vegetation: 1")
        st.write("- Moderate Vegetation: 1")
        st.write("- Sparse Vegetation: 1")
    
    if show_density:
        st.subheader("Population Density")
        st.write("Showing estimated population density heatmap")
        st.write("Red: High Density")
        st.write("Green: Medium Density")
        st.write("Blue: Low Density")

# Footer
st.markdown("---")
st.markdown("""
Data sources:
- Base Map: OpenStreetMap
- Sample data for demonstration
""")

import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load a Lottie animation from a URL
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load the Lottie animation (Example URL from LottieFiles)
lottie_animation_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_animation = load_lottie_url(lottie_animation_url)

# Streamlit app layout
st.title("Streamlit Lottie Animation Example")
st.write("This is a simple demo of using a Lottie animation in a Streamlit app.")

# Display the Lottie animation
st_lottie(
    lottie_animation,
    height=300,
    width=300,
    loop=True,
)

st.success("Lottie animation successfully loaded!")

