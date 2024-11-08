import streamlit as st
import folium
from streamlit_folium import folium_static

# Set page configuration
st.set_page_config(
    page_title="Erbil Urban Analysis Dashboard",
    page_icon="🏙️",
    layout="wide"
)

# Add title and description
st.title("Erbil Urban Analysis Dashboard")
st.markdown("""
This interactive dashboard visualizes various urban features in central Erbil.
Use the sidebar controls to explore different layers and data.
""")

# Create sidebar
st.sidebar.title("Map Controls")

# Add layer toggles in sidebar
show_landuse = st.sidebar.checkbox("Show Land Use", True)
show_roads = st.sidebar.checkbox("Show Roads", True)

# Create two columns
col1, col2 = st.columns([3, 1])

# Main map in column 1
with col1:
    # Create base map
    ERBIL_COORDS = [36.191111, 44.009167]
    m = folium.Map(location=ERBIL_COORDS, zoom_start=15)

    # Add Erbil Citadel marker
    folium.Marker(
        ERBIL_COORDS,
        popup="Erbil Citadel",
        tooltip="Erbil Citadel",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

    # Add sample landuse area (if checkbox is selected)
    if show_landuse:
        # Sample commercial area around citadel
        folium.Circle(
            ERBIL_COORDS,
            radius=200,  # 200 meters
            popup='Commercial District',
            color='red',
            fill=True,
            fillColor='red',
            fillOpacity=0.2
        ).add_to(m)

    # Add sample roads (if checkbox is selected)
    if show_roads:
        # Sample main road coordinates
        road_coords = [
            [[36.191111, 44.007167], [36.191111, 44.011167]],  # East-West road
            [[36.189111, 44.009167], [36.193111, 44.009167]]   # North-South road
        ]
        
        for coords in road_coords:
            folium.PolyLine(
                coords,
                color="blue",
                weight=3,
                opacity=0.8,
                popup="Main Road"
            ).add_to(m)

    # Display the map
    folium_static(m)

# Information panel in column 2
with col2:
    st.subheader("Area Information")
    st.write("""
    **Central Erbil Statistics:**
    - Area: ~2 km²
    - Major Landmark: Erbil Citadel
    - UNESCO World Heritage Site
    """)
    
    # Add time period selector
    st.subheader("Time Period")
    year = st.slider("Select Year", 2015, 2024, 2024)
    
    # Add information box
    st.info(f"""
    Showing data for: {year}
    
    The Erbil Citadel is one of the oldest 
    continuously inhabited sites in the world.
    """)

# Footer
st.markdown("---")
st.markdown("Data sources: OpenStreetMap (Base Map)")
