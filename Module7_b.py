#Module 7: Developing Web Maps and Representing information using Plots

import pandas as pd
import folium 
import os

os.getcwd()
os.chdir(r'C:\Users\PAVI\Desktop\Edureka\Python Certification\Module7')

#1 Display first 100 records from the data and play with parameters - tiles, zoom_start etc. 
#Map will be saved in BasicWebMap.html – view it in browser

data= pd.read_csv(r'539_m7_datasets_v1.0\539_m7_datasets_v1.0\Police_Department_Incidents_Year_2016_.csv',delimiter=',')
data.describe()
data.shape
data.info()
data.head(100)
top_100 = data[:100]

# Tiles can be Stamen Toner, OpenStreetMap, Mapbox Bright, Mapbox Control Room,Stamen Terrain
map = folium.Map(location=[37.773972,-122.431297],zoom_start=15,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='Police_Department_Incidents')

lat = list(top_100['Y'])
lon = list(top_100['X'])
add = list(top_100['Address'])
dist = list(top_100['PdDistrict'])

for la,lo,add in zip(lat,lon,add):    
    fg.add_child(folium.Marker(location=[la,lo],radius=6,popup=add,icon=folium.Icon(color='cadetblue')))

map.add_child(fg)

map.save('BasicWebMap.html')

#2 For latest 7 days of data create WebMap of Crimes which are categorized as ROBBERY

sorted_data = data.sort_values('Date',ascending=False)

robbery_data = sorted_data[sorted_data['Category']=='ROBBERY'][:7]

map = folium.Map(location=[37.773972,-122.431297],zoom_start=15,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='Robbery_Incidents')

lat = list(robbery_data['Y'])
lon = list(robbery_data['X'])
add = list(robbery_data['Address'])
dist = list(robbery_data['PdDistrict'])

for la,lo,add in zip(lat,lon,add):    
    fg.add_child(folium.Marker(location=[la,lo],radius=6,popup=add,icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save('Robberydetails.html')

#3 For latest 15 days of data create One WebMap of Crimes which are categorized as FRAUD and GAMBLING. 
# Change the icon to font awesome icon

fraud_gambling_data = sorted_data[((sorted_data['Category']=='FRAUD') | (sorted_data['Category']=='GAMBLING'))][:15]

#fraud_gambling_data = sorted_data[((sorted_data['Category']=='FRAUD') | (sorted_data['Category']=='GAMBLING'))]


map = folium.Map(location=[37.773972,-122.431297],zoom_start=15,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='Fraud_gambling_Incidents')

lat = list(fraud_gambling_data['Y'])
lon = list(fraud_gambling_data['X'])
add = list(fraud_gambling_data['Address'])
dist = list(fraud_gambling_data['PdDistrict'])
cat = list(fraud_gambling_data['Category'])

def color_producer(category):
    if category=='FRAUD':
        return 'red'
    else:
        return 'orange'
        
#for la,lo,add,cat,dist in zip(lat,lon,add,cat,dist):    
#    fg.add_child(folium.CircleMarker(location=[la,lo],radius=15,popup=str(add)+','+str(dist),fill_color=color_producer(cat), fill=True,color='Grey',fill_opacity=0.7))
#
#map.add_child(fg)
#map.add_child(folium.LayerControl())
#
#map.save('Fraudgamblingdetails.html')


for la,lo,add,cat,dist in zip(lat,lon,add,cat,dist):    
    fg.add_child(folium.Marker(location=[la,lo],radius=6,popup=str(add)+','+str(dist),fill_color=color_producer(cat), fill=True,color='Grey',fill_opacity=0.7,
                               icon=folium.Icon(color=color_producer(cat),icon='fa-exclamation-triangle',prefix='fa')))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save('Fraudgamblingdetails.html')


#4 BONUS ASSIGNMENT -- Display heatmap for Divvy Bikes. Divvy Bikes runs bike rental service in 
# Chicago and their bike station geolocation data is shared. Refer to BikesHeatMap.py and 
# Divvy_Stations_2016_Q3.csv, Divvy_Stations_2016_Q4.csv
import folium
import pandas as pd

Q3_data = pd.read_csv(r'539_m7_datasets_v1.0\539_m7_datasets_v1.0\Divvy_Stations_2016_Q3.csv',delimiter=',')
Q4_data = pd.read_csv(r'539_m7_datasets_v1.0\539_m7_datasets_v1.0\Divvy_Stations_2016_Q4.csv',delimiter=',')

map1 = folium.Map(location=[35,-80],zoom_start=10,tiles='Stamen Terrain')

fg_Q3 = folium.FeatureGroup(name='Divvy Stations 2016_Q3')

lat_Q3 = list(Q3_data['latitude'])
lon_Q3 = list(Q3_data['longitude'])
id_Q3 = list(Q3_data['id'])
name_Q3 = list(Q3_data['name'])

for la,lo,id,name in zip(lat_Q3,lon_Q3,id_Q3,name_Q3):
    fg_Q3.add_child(folium.CircleMarker(location=[la,lo],radius=10,popup=str(id)+','+str(name),color='green',fill_opacity=0.5))

fg_Q4 = folium.FeatureGroup(name='Divvy Stations 2016_Q4')

lat_Q4 = list(Q4_data['latitude'])
lon_Q4 = list(Q4_data['longitude'])
id_Q4 = list(Q4_data['id'])
name_Q4 = list(Q4_data['name'])

for la,lo,id,name in zip(lat_Q4,lon_Q4,id_Q4,name_Q4):
    fg_Q4.add_child(folium.CircleMarker(location=[la,lo],radius=5,popup=str(id)+','+str(name),color='yellow',fill_opacity=0.5))

map1.add_child(fg_Q3)
map1.add_child(fg_Q4)

map1.add_child(folium.LayerControl())
map1.save('Divvy_Stations_heatmap.html')

import folium
import pandas as pd

Q3_data = pd.read_csv(r'539_m7_datasets_v1.0\539_m7_datasets_v1.0\Divvy_Stations_2016_Q3.csv',delimiter=',')
Q4_data = pd.read_csv(r'539_m7_datasets_v1.0\539_m7_datasets_v1.0\Divvy_Stations_2016_Q4.csv',delimiter=',')


from folium import plugins
from folium.plugins import HeatMap

map_hooray = folium.Map(location=[35, -80],
                    zoom_start = 13) 

Q3_data['latitude'] = Q3_data['latitude'].astype(float)
Q3_data['longitude'] = Q3_data['longitude'].astype(float)


Q3 = Q3_data[['latitude', 'longitude']]

heat_data = [[row['latitude'],row['longitude']] for index, row in Q3.iterrows()]

HeatMap(heat_data).add_to(map_hooray)

map_hooray.save('Heatmap.html')

# Enhancements for code

BURGALRY_data = sorted_data[((sorted_data['Category']=='BURGLARY'))][:7]


map = folium.Map(location=[37.773972,-122.431297],zoom_start=15,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='Fraud_gambling_Incidents')

lat = list(BURGALRY_data['Y'])
lon = list(BURGALRY_data['X'])
add = list(BURGALRY_data['Address'])
dist = list(BURGALRY_data['PdDistrict'])


for la,lo,add,dist in zip(lat,lon,add,dist):    
    fg.add_child(folium.CircleMarker(location=[la,lo],radius=15,popup=str(add)+','+str(dist),fill_color='yellow', fill=True,color='Grey',fill_opacity=0.7))

map.add_child(fg)


map.save('Burgalrydetails.html')