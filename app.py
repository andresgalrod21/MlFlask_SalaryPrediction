from flask import Flask, render_template, request
from Modelo import predecir_salario

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    salario_anual = None
    salario_mensual = None

    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            genero = request.form["genero"]
            educacion = request.form["educacion"]
            experiencia = float(request.form["experiencia"])

            salario_anual, salario_mensual = predecir_salario(edad, genero, educacion, experiencia)
        except Exception as e:
            salario_anual = f"Error: {e}"

    return render_template("index.html", salario_anual=salario_anual, salario_mensual=salario_mensual)


if __name__ == "__main__":
    app.run(debug=True)
