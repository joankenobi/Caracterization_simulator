import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import pandas as pd

def crear_tabla(rangMin,rangMax,NumMuestras):
  """
    Crea la Tabla simulando la captura de datos.
  """
  varTransmisor=np.array([]) #Datos que lee el transmisor
  Alteraciones=np.random.rand(100)*10 #Diferentes estados del elemento a controlar.
  transmisorMuestras = np.linspace(rangMin,rangMax,NumMuestras) # Inicio, fin y cantidad de datos // Cantidad de muestras y rangos del transmisor
  actuador=np.array([np.linspace(0,100,NumMuestras)])
 
  for i in transmisorMuestras: #para cada dato del array, filtra los max y min, sumas un valor rand al resto.
    if i > rangMin:
      data=random.rand()
      i=i+data
    varTransmisor=np.append(varTransmisor,i)

  #1 crear listas que contengan actuador, variabletrasmisor*alteracion[1], ....[2], ...[n]
  data_array=np.array([varTransmisor*Alteraciones[i] for i in range(100)])
  #actuador_array= np.array([actuador])
  all_data=np.concatenate((actuador, data_array)).transpose()
  
  #2 crear las columnas actuador, variabletrasmisor*alteracion[1], ....[2], ...[n]
  columns_alts=["actuador"]+[f"Alt{i+1}: {Alteraciones[i]}" for i in range(100)]
  tabla= pd.DataFrame(columns=columns_alts,data=all_data)
  return tabla

def graficar_tabla(tabla, nombre=None):
  for i in range(1,len(tabla.columns)):
    plt.plot(tabla[tabla.columns[0]], tabla[tabla.columns[i]], color=(np.random.rand(),np.random.rand(),np.random.rand()))
    plt.xlabel("Actuador")
    plt.ylabel('Medición')
    plt.title(nombre)
  #plt.plot(20,20, "xr")
  plt.grid()
  plt.show()

def caracterizar( tabla, set_point, num_alteracion, rang_min=0, rang_max=100 ):
  """
    ----Imprime la apertura para un sep point y una alteracion------
  """
  if set_point>=rang_min and set_point<=rang_max: 

    idx_nearpos=(np.abs(tabla[tabla.columns[num_alteracion]]-set_point)).argmin()
    return print("Actuador:", round(tabla.actuador[idx_nearpos],2),"%", 
                 "    Transmisor:", (tabla[tabla.columns[num_alteracion]])[idx_nearpos], 
                 "   Alteracion:", tabla.columns[num_alteracion])
  else:
    return print("Set point:", set_point, "fuera de rango")

