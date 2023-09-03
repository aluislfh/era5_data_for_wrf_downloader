import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
from datetime import datetime

# Carga el fichero
ds = Dataset('download.nc', 'r')

# Carga las variables
lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
mslp = ds.variables['msl'][:]  # Mean sea level pressure
u10 = ds.variables['u10'][:]  # 10m u-component of wind
v10 = ds.variables['v10'][:]  # 10m v-component of wind
times = ds.variables['time'][:]  # Tiempos

# Calcula la magnitud del viento
wind_speed = np.sqrt(u10**2 + v10**2)

# Función para convertir las horas desde una fecha de referencia a un objeto datetime
def hours_since_to_datetime(hours_since_ref): # , ref_date_str="%Y-%m-%d %H:%M:%S"
    # ref_date = datetime.strptime(ds.variables['time'].units[11:], ref_date_str)
    # return ref_date + timedelta(hours=float(hours_since_ref))
    tout = ['2023-08-10_10:00', '2023-08-10_11:00', '2023-08-10_12:00', '2023-08-10_13:00', '2023-08-10_14:00', '2023-08-10_15:00', '2023-08-10_16:00', '2023-08-10_17:00']
    return tout[hours_since_ref]


for time_idx in range(len(times)):
    mslp_t = mslp[time_idx]
    wind_speed_t = wind_speed[time_idx]
    current_time = hours_since_to_datetime(time_idx)
    # current_time = hours_since_to_datetime(times[time_idx])

    # Crea un gráfico
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.coastlines()

    plt.title(f'MSLP y Wind Speed para {current_time}')
    clevs = np.array([990,995,1000,1005,1010,1015,1020,1025,1030,1035])
    
    # Plotea el sombreado para Mean sea level pressure
    c = ax.contourf(lons, lats, mslp_t/100, clevs, transform=ccrs.PlateCarree(), cmap='coolwarm_r')
    # plt.colorbar(c, ax=ax, orientation='vertical', label='MSLP (Pa)')

    # Plotea los bastagos para la velocidad del viento
    quiver = ax.quiver(lons[::5], lats[::5], u10[time_idx, ::5, ::5]/np.average(u10[time_idx, ::5, ::5]), v10[time_idx, ::5, ::5]/np.average(v10[time_idx, ::5, ::5]), 
                      wind_speed_t[::5, ::5], scale=1000, transform=ccrs.PlateCarree(), cmap='viridis')
    # plt.colorbar(quiver, ax=ax, orientation='vertical', label='Wind Speed (m/s)')


    # Ajusta los límites del mapa al área del océano Índico
    ax.set_extent([20, 85, -10, 35], crs=ccrs.PlateCarree())

    # Ajusta el alto de la barra de colores al alto del mapa
    posn = ax.get_position()
    colorbar_ax = fig.add_axes([posn.x0 + posn.width + 0.01, posn.y0, 0.04, posn.height])
    fig.colorbar(c, cax=colorbar_ax, orientation='vertical', label='MSLP (Pa)')
    # fig.colorbar(quiver, cax=colorbar_ax, orientation='vertical', label='Wind Speed (m/s)')

    plt.savefig(f"output_{time_idx}.png")
    plt.close()

ds.close()

