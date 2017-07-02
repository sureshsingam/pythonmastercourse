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

map.add_child(fg)

map.save("FrederictonBaseMap_CircleMarkers.html")
