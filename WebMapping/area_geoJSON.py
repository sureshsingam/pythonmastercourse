import folium
import pandas


def color_producer(h):

    if h <= 1000:
        return 'green'
    elif h> 1000 and h <=2000:
        return 'lightblue'
    else:
        return 'red'


#loading data from external file using pandas
data = pandas.read_csv("Volcanoes.txt")
#split the data so that lat and long are stored in separate lists
latitude = data.iloc[:,8] # this can also be accomplished by doing data["LAT"]
# Name of columns to be used can be found by data.columns
#convert latitude data frame to latitude(list)

latitude = list(latitude)

#do the same for longitude
longitude = data.iloc[:,9]
longitude = list(longitude)

#get elevation data
elev = list(data["ELEV"])

#get name data
name = list(data["NAME"])

#get location data
v_loc = list(data["LOCATION"])

#pair the  latitude and longitude in a same list by zipping them together
result = zip(latitude,longitude,elev,name,v_loc)

map = folium.Map(location=[45.9636,-66.6431],zoom_start=6, tiles="Mapbox Bright")

# Use feature group instead. As you can add multiple object types to a feature group

fg = folium.FeatureGroup(name="My Map")



#Adding markers at different coordinates
for x,y,h,v_name,loc in result:
    popupStr= "Elevation for {1}\n located in {2}\n is: {0}m".format(h,v_name,loc)
    fg.add_child(folium.CircleMarker(location=[x,y],radius=3,color=color_producer(h),weight=2,fill_color=color_producer(h),fill_opacity=0.5,popup=folium.Popup(popupStr)))

# Added feature group for polygon
fg_poly_layer = folium.FeatureGroup(name="Polygon Layer")
# add polygon by using folium.GeoJson()
fg_poly_layer.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),
                                    style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 1000000
                                                               else 'blue' if  x['properties']['POP2005'] >=1000000 and  x['properties']['POP2005'] < 30000000
                                                               else 'orange' if x['properties']['POP2005'] >=3000000 and  x['properties']['POP2005'] < 50000000
                                                               else 'red'},
                                    name="Area Polygon",control=True) )


map.add_child(fg)
map.add_child(fg_poly_layer)
map.add_child(folium.LayerControl())
map.save("area_Poly_with_CircleMarkers.html")
