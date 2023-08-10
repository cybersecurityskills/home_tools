from flask import Flask, request
import ssl

import os 

app = Flask(__name__)

@app.route("/")
def default():
   return("A web page!")

if __name__=="__main__":
   
  app.run(host='0.0.0.0',port=80)
