from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/tareas")
def tareas():
    return render_template("tareas.html")

if __name__ == "__main__":
    app.run(debug=True)