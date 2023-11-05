import folium
from folium.plugins import HeatMap
import pandas as pd


m = folium.Map(location=[24.68773, 46.72185], zoom_start=6)

# data = pd.read_csv(r'C:\Users\yazya\Desktop\heat-map\location_data.csv')
# data = pd.read_csv('C:\Users\yazya\Desktop\heat-map\book2222.csv')


data = pd.read_csv(r'C:\Users\yazya\Desktop\heat-map\book2222.csv')

# "C:\Users\yazya\Desktop\heat-map\book2222.csv"


# data =pd.read_csv("C:\Users\yazya\Desktop\Book2.csv")

heat_data = data[['lat', 'lng']].values

HeatMap(heat_data).add_to(m)

m.save('heatmap.html')


