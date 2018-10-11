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

def tratarNAN(df,nombreVar="",valorReemp=""):
    '''Función para tratar los valores perdidos dentro del dataset.
    Devuelve un dataset con los valores perdidos ya procesados
    
    Variables:
         @paramdf -> Dataframe a procesar para eliminar valores perdidos
         @param nombreVar -> Variables que queremos chequear para procesar valores perdidos
    '''
    df.dropna(axis=1,how="all")
    df.dropna(axis=0,how="all").shape
    if df[nombreVar].dtype != "int64" and df[nombreVar].dtype != "float64":
        print("La variable es detectada como un objeto y no puede ser procesada")
    else:
        salida=False
        while not salida:
            procesado = int(input("""Selecciona el tipo de procesado: 
                              \n\t1 - Substituir los NaN por el valor proporcionado {}
                              \n\t2 - Substituir los NaN por la media
                              \n\t3 - Substituir los NaN por la mediana
                              \n\t4 - Substituir los NaN por el primer valor conocido hacia adelante
                              \n\t5 - Substituir los NaN por el primer valor conocido hacia atrás
                              """.format(valorReemp)))
            if procesado == 1:
                df = df[nombreVar].fillna(valorReemp)
                salida=True
            elif procesado == 2:
                df[nombreVar]=df[nombreVar].fillna(df[nombreVar].mean())
                salida=True
            elif procesado == 3:
                df[nombreVar]=df[nombreVar].fillna(df[nombreVar].median())
                salida=True
            elif procesado == 4:
                df[nombreVar] = df[nombreVar].fillna(method="ffill")
                salida=True
            elif procesado == 5:
                df[nombreVar] = df[nombreVar].fillna(method="bfill")
                salida=True
            else:
                print("debe seleccionar una opción")
    return df
    
    
    
    
def crearDummies(df,nombreVar):
    dummy_var = pd.get_dummies(df[nombreVar], prefix=nombreVar)
    df = df.drop(columns=nombreVar)
    df =pd.concat([df,dummy_var], axis=1)
    return df

