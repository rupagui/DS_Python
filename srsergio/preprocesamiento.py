#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 22:39:57 2018

@author: serranos
"""
import pandas
import urllib3

def downloadfromURL(url,method="GET",path="./",filename="descarga",sep=",",delim="\n"):
    http = urllib3.PoolManager()
    response = http.request(method,url)
    if response.status != 200:
        print("No se ha podido descargar el fichero dela URL {}".format(url))
        return None
    else:
        datos = response.data.decode('utf-8')
        lista=datos.split(delim)
        outfile = path + "/" + filename + ".csv"
        with open(outfile,"w") as outfile1:
            for i in range(len(lista)):
                outfile1.write(lista[i])
                outfile1.write("\n")
        
        df=pandas.read_csv(outfile)
        df.to_excel(path + "/" + filename + ".xls")
        df.to_json(path + "/" + filename + ".json")
    return df

medals_df = downloadfromURL(url="http://winterolympicsmedals.com/medals.csv")
medals_df.head()