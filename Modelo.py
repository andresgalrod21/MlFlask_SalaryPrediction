import pickle
import numpy as np

# Cargar modelo entrenado
with open("modelo_salario.pkl", "rb") as f:
    modelo = pickle.load(f)

# Cargar encoders
with open("encoder_genero.pkl", "rb") as f:
    encoder_genero = pickle.load(f)

with open("encoder_educacion.pkl", "rb") as f:
    encoder_educacion = pickle.load(f)

def predecir_salario(edad, genero, educacion, experiencia):
    # Codificar género y educación
    genero_cod = encoder_genero.transform([genero])[0]
    educacion_cod = encoder_educacion.transform([educacion])[0]

    # Crear vector de entrada
    entrada = np.array([[edad, genero_cod, educacion_cod, experiencia]])

    # Hacer la predicción (salario anual)
    salario_anual = modelo.predict(entrada)[0]
    salario_mensual = salario_anual / 12

    return round(salario_anual, 2), round(salario_mensual, 2)
