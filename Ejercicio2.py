import matplotlib.pyplot as plt
import pandas as pd
#enlace al dataset: https://www.kaggle.com/datasets/pradeepjangirml007/laptop-data-set
"""
Este dataset contiene especificaciones detalladas de 3.976 portátiles de diversas marcas. 
Los datos incluyen una variedad de características como marca, detalles del procesador, RAM, 
opciones de almacenamiento, información de la GPU, tipo de pantalla, precio y duración de la batería. 
Puede resultar útil para explorar y analizar las especificaciones de portátiles de diferentes rangos 
de precios y configuraciones.
"""
#mandar a llamar el arcivo
df = pd.read_csv("laptop.csv")
