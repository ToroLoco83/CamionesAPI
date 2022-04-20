from flask import Flask, current_app, flash, render_template, request, redirect, send_file, send_from_directory, url_for


#Iniciar app de flask
app = Flask(__name__)


@app.route("https://toroloco83.github.io/CamionesAPI/API")
def home():
    return 'HOLA MUNDO'
