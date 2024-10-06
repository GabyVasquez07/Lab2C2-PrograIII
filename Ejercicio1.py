import matplotlib.pyplot as plt
import pandas as pd
#enlace al dataset: https://kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset
"""
Este conjunto de datos ofrece una visión detallada de las rutinas de ejercicio, los atributos físicos 
y las métricas de forma física de los socios de un gimnasio. Contiene 973 muestras de datos de gimnasios,
incluidos indicadores clave de rendimiento como la frecuencia cardiaca, las calorías quemadas y la 
duración del entrenamiento. Cada entrada incluye también datos demográficos y niveles de experiencia,
lo que permite un análisis exhaustivo de los patrones de forma física, la progresión de los deportistas
y las tendencias de salud.
"""
#mandar a llamar el arcivo
df = pd.read_csv("gym_members_exercise_tracking.csv")

#crear la frecuencia, trabajamos con la informacion de frecuencia de entrenamiento, dias a la semana 
fr = df["Workout_Frequency (days/week)"].value_counts()

#colores
colores = ["#73c6b6","#f9e79f","#d2b4de","#e6b0aa"]

#creacion del grafico tipo pastel
plt.pie(fr.values, labels=fr.index, autopct="%1.1f%%",colors=colores)
plt.title("Frecuencia de Entrenamiento (dias a la semana)")#titulo

plt.show()
