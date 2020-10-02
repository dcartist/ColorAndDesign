from flask import Flask, jsonify, request
import json
from colors import colorData
with open('newColors.json') as colorlisting:
  # data = colorlisting.read()
  data = json.load(colorlisting)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/')
def index():
    return "Colors"
@app.route('/colors')
def colors():
    # colorData = json.dumps(data, indent=4)
    # colorlisted = []
    # for color in data:
    #   colorlisted.append(color)
    # return jsonify(colorData)
    colorlisted = []
    for color in colorData:
      colorlisted.append(color)
    return jsonify(colorlisted)
    # return jsonify(colorData)
@app.route('/colors/search/<name>', methods=['GET'])
def colornames(name=None):
  if request.method =='GET':
    if name:
      colorlisted = []
      for color in colorData:
        if name == color['name']:
         colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
@app.route('/colors/digit/<name>', methods=['GET'])
def colornamesByLetter(name=None):
  if request.method =='GET':
    if name:
      colorlisted = []
      for color in colorData:
        if name[0] == color['name'][0]:
         colorlisted.append(color)
      return(jsonify(colorlisted))
      # return f"{name} is something"
    else:
      return data
      
app.run(port=3000, debug=True)