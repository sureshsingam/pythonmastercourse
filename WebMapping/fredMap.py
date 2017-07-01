import folium
map = folium.Map(location=[45.9636,-66.6431],zoom_start=6, tiles="Mapbox Bright")

# Use feature group instead. As you can add multiple object types to a feature group

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[45.9849785,-66.6642852],popup=folium.Popup('My Home'),icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("FrederictonBaseMap_AddMarkers.html")
