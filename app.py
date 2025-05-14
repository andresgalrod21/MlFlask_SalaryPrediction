from flask import Flask, render_template, request
from Modelo import predecir_salario

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            genero = request.form["genero"]
            educacion = request.form["educacion"]
            experiencia = float(request.form["experiencia"])

            resultado = predecir_salario(edad, genero, educacion, experiencia)
        except Exception as e:
            resultado = f"Error en los datos: {e}"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
