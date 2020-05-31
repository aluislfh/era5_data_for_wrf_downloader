Adaptación de los scripts publicados en https://dreambooker.site/2019/10/03/Initializing-the-WRF-model-with-ERA5-pressure-level/ para realizar descargas a traves de una conexion de un servidor proxy. Los scripts ya disponen de todas las variables y parámetros necesarios para correr el modelo WRF.
Pasos para su uso:
Instalar la biblioteca de python --> "cdsapi"
para eso puedes usar pip --> /home/adrian/anaconda3/bin/pip --proxy=http://usuario:contraseña@PROXY_IP:PORT install cdsapi
el fichero ".cdsapirc" debes ponerlo en tu HOME (debe tener los datos de tu cuenta de usuario)
el script que vas a correr y necesitas editar es --> "download.sh"
en ese fichero lo que falta por precisar es la fecha inicial y final, y el área geográfica cuando lo corras ya dentro se llaman a los dos scripts de python que estan en el directorio, que son --> "GetERA5-sl.py" y "GetERA5-pl.py", el script de bash los toma como plantilla y crea nuevos scripts donde inserta los parámetros de fecha y límites geográficos.
otra cosa que debes cambiar es al inicio del script de bash estas líneas de acuerdo al enviroment y paths de la pc donde lo vayas a correr:

    CODEDIR=/home/adrian/Desktop/prueba
    DATADIR=/home/adrian/Desktop/prueba/data

    # Set your python environment
    export PATH=/home/adrian/anaconda3/bin:$PATH

cuando completes estos pasos ya puedes ejecutar el script de bash --> "bash download.sh"
