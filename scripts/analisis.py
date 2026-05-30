import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer los datos
df = pd.read_csv('datos/dataset.csv')

# 2. Encontrar las temperaturas máximas y mínimas
indice_calor = df['Mean'].idxmax()
indice_frio = df['Mean'].idxmin()

# Usamos .loc para buscar la temperatura y el año/mes exacto en esas posiciones
temp_max = df.loc[indice_calor, 'Mean']
fecha_max = df.loc[indice_calor, 'Year']

temp_min = df.loc[indice_frio, 'Mean']
fecha_min = df.loc[indice_frio, 'Year']

# 3. Mostrar los resultados en pantalla
print("=== RESULTADOS DEL ANÁLISIS CLIMÁTICO ===")
print(f"Hizo mas calor en la fecha {fecha_max} con una maxima de {temp_max}.")
print(f"Hizo mas frío en la fecha {fecha_min} con una minima de {temp_min}.")
print("=========================================")

# 4. Crear un gráfico simple de evolución de temperatura
plt.figure(figsize=(10, 5))

plt.plot(df['Year'], df['Mean'], color='orange', linewidth=0.5)

plt.title('Evolución de las Temperaturas Globales')
plt.xlabel('Año y Mes')
plt.ylabel('Temperatura Promedio')

# Ocultar las etiquetas del eje X porque son demasiados años y se amontonan
plt.xticks([]) 

# 5. Guardar el resultado
plt.savefig('resultados/grafico_resultados.png')
plt.close()
