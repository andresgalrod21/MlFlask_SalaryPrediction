import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Cargar datos
df = pd.read_csv("SalaryData.csv")  

# Limpieza
df = df.dropna()

encoder_gender = LabelEncoder()
encoder_edu = LabelEncoder()

df['Gender'] = encoder_gender.fit_transform(df['Gender'])  # Male=1, Female=0 (por ejemplo)
df['Education Level'] = encoder_edu.fit_transform(df['Education Level'])

# Variables predictoras y objetivo
X = df[['Age', 'Gender', 'Education Level', 'Years of Experience']]
y = df['Salary']

modelo = LinearRegression()
modelo.fit(X, y)

with open("modelo_salario.pkl", "wb") as f:
    pickle.dump(modelo, f)

with open("encoder_genero.pkl", "wb") as f:
    pickle.dump(encoder_gender, f)

with open("encoder_educacion.pkl", "wb") as f:
    pickle.dump(encoder_edu, f)

print("Modelo y encoders entrenados y guardados.")
