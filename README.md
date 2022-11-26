# ControlHubSoftEng

#Primero expotamos Flask y request
from flask import Flask, request
#Luego creamos una instancia de flask
app = Flask(__name__)

#Armamos la función de fibonacci
def fibo(n: int):
  if n < 1:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

#Definimos la ruta principal y listo podemos usarlo y 
@app.route("/")
def fibonaci():
  return str(fibo(int(request.args['n'])))
