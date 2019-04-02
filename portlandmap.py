from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('mapping_coordinates.csv')

print()

# m = Basemap(projection='mill',
#             llcrnrlat = 45.417749,
#             llcrnrlon = -122.822203,
#             urcrnrlat = 45.643937,
#             urcrnrlon = -122.484606,
#             resolution = 'f')
# # m.fillcontinents()
# m.drawrivers()
# m.drawcoastlines()
#
# plt.title('portland')
# plt.show()
