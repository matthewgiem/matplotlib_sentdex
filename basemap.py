from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# https://matplotlib.org/basemap/ for documentation for Basemap
m = Basemap(projection='mill')
# mill stands for Miller Cylindrical Projection
# more projections can be found at https://matplotlib.org/basemap/users/mapsetup.html
m.drawcoastlines()
m.fillcontinents()

plt.title('Basemap Tutorial')
plt.show()
