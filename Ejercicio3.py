import pandas as pd
import matplotlib.pyplot as plt
"""
Este dataset fue creado por un usuario en kaggle sobre un análisis de las redes sociales.
Según palabras del autor, los datos de este conjunto de datos se proporcionaron utilizando 
datos numéricos en la medida de lo posible. Se proporcionan usuarios ficticios, países, edad, 
horas promedio de uso de las redes sociales y número total de "me gusta".
"""

#Link del dataset: https://www.kaggle.com/datasets/hanaksoy/social-media-analysis

# Mandamos a llamar el dataset
df = pd.read_csv('social-media.csv')

# Agrupamos los datos por edad y sumamos los likes 
likesedad= df.groupby('Age')['TotalLikes'].sum().reset_index()

# Creamos el gráfico de líneas
plt.figure(figsize=(12, 6))                         #Utilizamos 'o' como marcador del gráfico de líneas y el color de las  líneas como celeste.
plt.plot(likesedad['Age'], likesedad['TotalLikes'], marker='o', color='skyblue')

# Añadimos el título y etiquetas
plt.title('Total de Likes por Edad', fontsize=16)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Total de Likes', fontsize=12)

# Ajustamos el diseño
plt.tight_layout()

# Mostramos el gráfico
plt.grid()  # Agregamos una cuadrícula, esto para mejor legibilidad
plt.show()

"""
Análisis:
En este dataset, representamos el total de likes por edad en las redes sociales,
mostrando en el eje y, el total de likes y en el eje x las edades. Y de acuerdo con el gráfico,
podemos concluir que las edades que comprenden entre los 18 y 20 años son las que más dan likes,
estando estos entre el rango de los 20 y 40 likes, y por contraparte, las personas en edades de
60 años no tienden a dar like a las publicaciones.

"""