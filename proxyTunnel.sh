#!/bin/bash

#USAGE: jodo wget https://google.com.cu

# Autores originales de este script para conexiones con servidores proxy:
#@migulelespauljr, @javier.cabrales, @engel

if [ -z $1 ]; then 
 echo "USAGE: jodo -u [USERNAME] [STATMENT] or jodo [STATMENT]"
 exit
elif [ $1 == "-u" ]; then 
 read -p "user: " -s PASS
 read -p "password: " -s PASS
else
 USER='TU_USUARIO'
 read -p "USUARIO ${USER} ESCRIBE EL PASSWORD: " -s PASS
fi 

if [ $1 == "-proxy2" ]; then
 # EL SEGUNDO PROXY ES OPCIONAL

 export http_proxy=http://${USER}:${PASS}@IP_PROXY2:PORT2/
 export https_proxy=http://${USER}:${PASS}@IP_PROXY2:PORT2/
 export ftp_proxy=http://${USER}:${PASS}@IP_PROXY2:PORT2/
 export HTTP_PROXY=http://${USER}:${PASS}@IP_PROXY2:PORT2/
 export HTTPS_PROXY=http://${USER}:${PASS}@IP_PROXY2:PORT2/
 export FTP_PROXY=http://${USER}:${PASS}@IP_PROXY2:PORT2/ 
 $2 $3 $4 $5 $6 $7 $8
else
 echo "proxy1"
 export http_proxy=http://${USER}:${PASS}@IP_PROXY1:PORT1/
 export https_proxy=http://${USER}:${PASS}@IP_PROXY1:PORT1/
 export ftp_proxy=http://${USER}:${PASS}@IP_PROXY1:PORT1/
 export HTTP_PROXY=http://${USER}:${PASS}@IP_PROXY1:PORT1/
 export HTTPS_PROXY=http://${USER}:${PASS}@IP_PROXY1:PORT1/
 export FTP_PROXY=http://${USER}:${PASS}@IP_PROXY1:PORT1/ 
 $@
fi

