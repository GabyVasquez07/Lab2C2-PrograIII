import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#enlace al dataset: https://www.kaggle.com/datasets/pradeepjangirml007/laptop-data-set
"""
Este dataset contiene especificaciones detalladas de 3.976 portátiles de diversas marcas. 
Los datos incluyen una variedad de características como marca, detalles del procesador, RAM, 
opciones de almacenamiento, información de la GPU, tipo de pantalla, precio y duración de la batería. 
Puede resultar útil para explorar y analizar las especificaciones de portátiles de diferentes rangos 
de precios y configuraciones.
"""
#mandamos a llamar el arcivo
df = pd.read_csv("laptop.csv")

# Contamos el número de laptops por marca
brand_counts = df["Brand"].value_counts()

# Creamos el gráfico de barras
plt.figure(figsize=(10, 6))  # Ajustamos el tamaño de la gráfica
brand_counts.plot(kind='bar', color='lightblue')
#Definimos que queremos un gráfico de barras y que las barras sean color celeste

# Añadimos título y etiquetas
plt.title("Número de laptops por marca", fontsize=16)
plt.xlabel("Marca", fontsize=12)
plt.ylabel("Número de laptops", fontsize=12)

# Rotamos las etiquetas para mayor legibilidad
plt.xticks(rotation=45, ha="right")

# Ajustamos el diseño
plt.tight_layout()

# Mostramos gráfico
plt.show()

