import pandas as pd
import matplotlib.pyplot as plt  # Importar la librería para graficar

# Ruta del archivo CSV
file_path = 'meteo.csv'

# Leer el archivo CSV
df = pd.read_csv(file_path)

# Graficar las columnas 'X1' y 'y'
plt.plot(df['X1'], df['y'], marker='o', linestyle='-', color='b', label='X1 vs y')

# Etiquetas y título
plt.xlabel('X1')  # Etiqueta del eje X
plt.ylabel('y')   # Etiqueta del eje Y
plt.title('Gráfico de X1 vs y')  # Título del gráfico

# Mostrar leyenda y cuadrícula
plt.legend()
plt.grid(True)

# Guardar el gráfico como imagen JPG
plt.savefig('grafico.jpg', format='jpg')

# Mostrar el gráfico en pantalla
plt.show()

# Mostrar los primeros datos para verificar
print(df.head())
