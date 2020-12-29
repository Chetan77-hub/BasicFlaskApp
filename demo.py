from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Welcome To Flask app Created on 29 DEc 2020"

if (__name__) == "__main__":
  app.run(host = '0.0.0.0' ,port=5001,debug=True)
 
