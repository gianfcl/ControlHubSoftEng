# ControlHubSoftEng

#Primero expotamos Flask y request<br>
from flask import Flask, request<br>
#Luego creamos una instancia de flask<br>
app = Flask(__name__)<br>

#Armamos la función de fibonacci<br>
def fibo(n: int):<br>
  if n < 1:<br>
    return 0<br>
  elif n == 1:<br>
    return 1<br>
  else:<br>
    return fibo(n-1)+fibo(n-2)<br>

#Definimos la ruta principal y listo podemos usarlo y <br>
@app.route("/")<br>
def fibonaci():<br>
  return str(fibo(int(request.args['n'])))
