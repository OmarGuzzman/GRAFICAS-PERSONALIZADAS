import pandas as pd
import matplotlib.pyplot as plt  

# Cargar datos
df = pd.read_csv('ventas_tienda.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Ingresos'] = df['Cantidad Vendida'] * df['Precio']

# Gráfico de tendencias de ventas
plt.figure(figsize=(12, 6))
df.set_index('Fecha').resample('M').sum()['Ingresos'].plot(linewidth=2, color='blue')
plt.title('Tendencias de Ventas Mensuales', fontsize=14)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Ingresos', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import seaborn as sns 

# Gráfico de ventas por categoría
plt.figure(figsize=(12, 6))
sns.barplot(x='Categoría', y='Ingresos', data=df.groupby('Categoría').sum().reset_index(), palette='viridis')
plt.title('Ventas Totales por Categoría', fontsize=14)
plt.xlabel('Categoría', fontsize=12)
plt.ylabel('Ingresos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Histograma de distribución de ingresos
plt.figure(figsize=(12, 6))
plt.hist(df['Ingresos'], bins=30, edgecolor='black', color='skyblue', alpha=0.7)
plt.title('Distribución de Ingresos por Rango de Ventas', fontsize=14)
plt.xlabel('Ingresos', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.tight_layout()
plt.show()





