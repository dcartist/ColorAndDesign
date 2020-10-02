from flask import Flask, jsonify, request
import json
from colors import colorData
with open('newColors.json') as colorlisting:
  data = json.load(colorlisting)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/')
def index():
    return "Colors"
@app.route('/colors')
def colors():
    colorlisted = []
    for color in colorData:
      colorlisted.append(color)
    return jsonify(colorlisted)
    
@app.route('/colors/search/<name>', methods=['GET'])
def colornames(name=None):
  if request.method =='GET':
    if name:
      colorlisted = []
      for color in colorData:
        if name == color['name'] or name.lower() == color['name'].lower():
         colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
@app.route('/colors/id/<id>', methods=['GET'])
def colorbyid(id=None):
  if request.method =='GET':
    if id:
      colorlisted = []
      for color in colorData:
        if int(id) == color['id']:
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
        if name[0] == color['name'][0] or name[0].lower() == color['name'][0].lower():
         colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
@app.route('/colors/snippet/<snippet>', methods=['GET'])
def colornamesBysnipet(snippet=None):
  if request.method =='GET':
    if snippet:
      colorlisted = []
      for color in colorData:        
        if snippet in color["name"] or snippet.lower() in color["name"].lower():
          colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
@app.route('/colors/hex/snippet/<snippet>', methods=['GET'])
def colornamesByHexsnipet(snippet=None):
  if request.method =='GET':
    if snippet:
      colorlisted = []
      for color in colorData:        
        if snippet in color["hex"] or snippet.lower() in color["hex"].lower():
          colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
@app.route('/colors/hex/code/<name>', methods=['GET'])
def colorsbyHex(name=None):
  if request.method =='GET':
    if name:
      colorlisted = []
      for color in colorData:
        if name == color['hex'][1:] or name.lower() == color['hex'][1:].lower():
         colorlisted.append(color)
      return(jsonify(colorlisted))
    else:
      return "Insert Color Data"
app.run(port=3000, debug=True)