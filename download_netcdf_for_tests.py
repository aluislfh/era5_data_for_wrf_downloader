import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', 'mean_sea_level_pressure',
        ],
        'year': '2023',
        'month': '08',
        'day': '10',
        'time': [
            '10:00', '11:00', '12:00',
            '13:00', '14:00', '15:00',
            '16:00',
        ],
        'format': 'netcdf',
    },
    'download.nc')
