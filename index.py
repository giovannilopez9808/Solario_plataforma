from flask import Flask, render_template, request, redirect, url_for, flash
from models import *
import datetime

today = datetime.date.today()
app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')
app.secret_key = "mykey"


@app.route('/')
def home():
    """
    Render de la pagina principal
    """
    return render_template("home.html", today=today)


@app.route('/contact', strict_slashes=False)
def error():
    """
    Render de la pagina de contacto
    """
    return render_template("contact.html")


@app.route("/information", strict_slashes=False)
def info():
    """
    Render de la pagina de informacion
    """
    return render_template("information.html")


@app.route('/room', methods=["POST"])
def room():
    """
    Render de la pagina de cabinas
    """
    if request.method == "POST":
        results = TES_solario(request)
    return render_template("cabin.html", results=results)


@app.route("/cloud", methods=["POST"])
def cloudtype():
    """
    Render de la pagina de condiciones de cielo
    """
    if request.method == "POST":
        results = TES_solario(request)
        results.get_data_cabin()
    return render_template("cloud.html", results=results)


@app.route("/recommend", methods=["POST"])
def cont():
    """
    Render de la pagina de resultados
    """
    if request.method == "POST":
        results = TES_solario(request)
        results.get_final_data()
    return render_template("results.html", results=results)


if __name__ == '__main__':
    app.run(debug=True)
