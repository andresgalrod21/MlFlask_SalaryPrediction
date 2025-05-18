import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import os

df = pd.read_csv("SalaryData.csv")
df = df.dropna()

X = df[["Years of Experience"]]
y = df["Salary"]

modelo = LinearRegression()
modelo.fit(X, y)

x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = modelo.predict(x_line)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Datos reales")
plt.plot(x_line, y_line, color="red", linewidth=2, label="Línea de regresión")
plt.title("Regresión lineal: Experiencia vs Salario")
plt.xlabel("Años de experiencia")
plt.ylabel("Salario (USD anual)")
plt.legend()
plt.grid(True)

os.makedirs("static", exist_ok=True)
plt.tight_layout()
plt.savefig("static/salario_vs_experiencia.png")
print("Gráfico guardado correctamente.")
