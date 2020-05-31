#!/bin/bash -l

CODEDIR=/home/adrian/Desktop/prueba
DATADIR=/home/adrian/Desktop/prueba/data

# Set your python environment
export PATH=/home/adrian/anaconda3/bin:$PATH
source activate root
cd $CODEDIR

DATE1=20170419
DATE2=20170420
YY1=`echo $DATE1 | cut -c1-4`
MM1=`echo $DATE1 | cut -c5-6`
DD1=`echo $DATE1 | cut -c7-8`
YY2=`echo $DATE2 | cut -c1-4`
MM2=`echo $DATE2 | cut -c5-6`
DD2=`echo $DATE2 | cut -c7-8`
Nort=35
West=-110
Sout=5
East=-55

sed -e "s/DATE1/${DATE1}/g;s/DATE2/${DATE2}/g;s/Nort/${Nort}/g;s/West/${West}/g;s/Sout/${Sout}/g;s/East/${East}/g;" GetERA5-sl.py > GetERA5-${DATE1}-${DATE2}-sl.py

./proxyTunnel.sh python GetERA5-${DATE1}-${DATE2}-sl.py

sed -e "s/DATE1/${DATE1}/g;s/DATE2/${DATE2}/g;s/Nort/${Nort}/g;s/West/${West}/g;s/Sout/${Sout}/g;s/East/${East}/g;" GetERA5-pl.py > GetERA5-${DATE1}-${DATE2}-pl.py

./proxyTunnel.sh python GetERA5-${DATE1}-${DATE2}-pl.py

mkdir -p ${DATADIR}/$YY1

mv ERA5-${DATE1}-${DATE2}-sl.grib ERA5-${DATE1}-${DATE2}-pl.grib ${DATADIR}/$YY1/


exit 0
