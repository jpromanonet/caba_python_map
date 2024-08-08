import folium
from IPython.display import IFrame, display

# Center the map on Buenos Aires, CABA
map_center = [-34.6037, -58.3816]
mymap = folium.Map(location=map_center, zoom_start=12)

# Add a marker for Buenos Aires
folium.Marker(
    [-34.6037, -58.3816],
    popup="Buenos Aires",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Save the map to an HTML file
mymap.save("buenos_aires_map.html")

# Display the HTML file
display(IFrame("buenos_aires_map.html", width=600, height=400))
