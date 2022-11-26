from flask import Flask, request
app = Flask(__name__)

def fibo(n: int):
  if n < 1:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)


@app.route("/")
def fibonaci():
  return str(fibo(int(request.args['n'])))
