from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv('mapping_coordinates.csv')

long = df['vehicle_location_longitude'].tolist()
lat = df['vehicle_location_latitude'].tolist()
lon_lat = []
for y in range(len(lat)):
    lon_lat.append([long[y], lat[y]])

# 45.526135, -122.675518
#
# m = Basemap(projection='mill',
#             llcrnrlat = 45.4,
#             llcrnrlon = -122.8,
#             urcrnrlat = 45.643937,
#             urcrnrlon = -122.484606,
#             resolution = 'f')
# # m.fillcontinents()
# m.plot(lon_lat[0], lon_lat[0], 'c*', markersize=15)
# m.drawrivers()
# m.drawcoastlines()
#
# plt.title('portland')
# plt.show()


output_path = "saved_maps"
i = 0
for x in range(len(lon_lat)):

    m = Basemap(projection='mill',
                llcrnrlat = 45.4,
                llcrnrlon = -122.8,
                urcrnrlat = 45.643937,
                urcrnrlon = -122.484606,
                resolution = 'f')
    # m.fillcontinents()
    m.plot(lon_lat[x], lon_lat[x], 'c*', markersize=15)
    m.drawrivers()
    m.drawcoastlines()

    plt.title('portland')

    filepath = os.path.join(output_path, 'portland' + str(i) + '.png')
    plt.savefig(filepath)
    i+=1
