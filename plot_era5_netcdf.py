import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset

# Carga el fichero
ds = Dataset('download.nc', 'r')

# Carga las variables
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
mslp = ds.variables['msl'][:]  # Mean sea level pressure
u10 = ds.variables['u10'][:]  # 10m u-component of wind
v10 = ds.variables['v10'][:]  # 10m v-component of wind

# Calcula la magnitud del viento
wind_speed = np.sqrt(u10**2 + v10**2)

# Selecciona el plazo de tiempo que quieras, por ejemplo el primero
time_idx = 0
mslp_t = mslp[time_idx]
wind_speed_t = wind_speed[time_idx]

# Crea un gráfico
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines()

# Plotea el sombreado para Mean sea level pressure
c = ax.contourf(lons, lats, mslp_t, transform=ccrs.PlateCarree(), cmap='coolwarm_r')
plt.colorbar(c, ax=ax, orientation='vertical', label='MSLP (Pa)')

# Plotea los bastagos para la velocidad del viento
quiver = ax.quiver(lons[::5], lats[::5], u10[time_idx, ::5, ::5], v10[time_idx, ::5, ::5], 
                  wind_speed_t[::5, ::5], scale=500, transform=ccrs.PlateCarree(), cmap='viridis')
# plt.colorbar(quiver, ax=ax, orientation='vertical', label='Wind Speed (m/s)')

plt.title(f'MSLP y Wind Speed para el tiempo {time_idx}')


plt.show()

ds.close()

