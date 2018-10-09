#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 22:39:57 2018

@author: serranos
"""
import pandas as pd
import urllib3

def procesaURL(url, method="GET", path="./", sep=",", delim="\n"):
    http = urllib3.PoolManager()
    response = http.request(method,url)
    if response.status != 200:
        print("No se ha podido descargar el fichero dela URL {}".format(url))
    else:
        datos = response.data.decode('utf-8')
        lista=datos.split(delim)
        cabecera=[]
        cabecera.append(lista[0].split(sep))
        #print(cabecera[0])
        datos1=[]
        for i in range(1,len(lista)):
            datos1.append(lista[i].split(sep))
        #print(datos1[0])
        df = pd.DataFrame.from_records(datos1,columns=cabecera)
        return df

