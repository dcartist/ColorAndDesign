from flask import Flask, jsonify, request
import json

with open('newColors.json') as colorlisting:
  data = json.load(colorlisting)

app = Flask(__name__)
@app.route('/')
def index():
    return "Colors"
@app.route('/colors')
def colors():
    return jsonify(data)
@app.route('/colors/<name>', methods=['GET'])
def colornames(name=None):
  if request.method =='GET':
    if name:
      # return(jsonify(data.name == name))
      colorlisted = []
      for color in data:
        if name == color['name']:
         colorlisted.append(color)
      return(jsonify(colorlisted))
      # return f"{name} is something"
    else:
      colorlisted = []
      for color in data:
        colorlisted.append(color)
        return(jsonify(colorlisted))

app.run(port=3000, debug=True)