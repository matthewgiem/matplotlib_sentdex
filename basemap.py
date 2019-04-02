from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# https://matplotlib.org/basemap/ for documentation for Basemap
m = Basemap(projection='mill',
            llcrnrlat = -90, #lower left corner latitude is llcrnrlat
            llcrnrlon = -180, #lower left corner longitude is llcrnrlon
            urcrnrlat = 90, # upper right corner latitude is urcrnrlat
            urcrnrlon = 180, # upper right corner longitude is urcrnrlon
            resolution = 'h') # crude = c low = l, high = h, full = f
# mill stands for Miller Cylindrical Projection
# more projections can be found at https://matplotlib.org/basemap/users/mapsetup.html
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
# m.drawcounties(zorder=20) # no fix for this yet
# m.fillcontinents(color='brown', lake_color='blue')
# m.etopo()
m.bluemarble()

plt.title('Basemap Tutorial')
plt.show()
