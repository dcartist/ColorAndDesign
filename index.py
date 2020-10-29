from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# from routes import request_api

import json
from colors import colorData
with open('newColors.json') as colorlisting:
  data = json.load(colorlisting)


# app = Flask(__name__)
app = Flask(__name__)
cors = CORS(app)
#Swagger info
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Colors By Design",
        'SwaggerUIStandalonePreset': {'TopbarPlugin': False}}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# app.register_blueprint(request_api.get_blueprint())


app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
@app.route('/api')
def apicolorFull():
  if request.method =='GET':    
    colorsinlist = []
    for color in colorData:
      if color["id"] < 1000:
      # for x in range(5):
        colorsinlist.append(color)
  # return "jsonify(colorsinlist)"
  return jsonify(colorsinlist)
# @app.route('/api')
# def api_index():
#   return render_template('api.html', colors = len(data))

@app.route('/', methods=['GET'])
def colorListDisplay():
  if request.method =='GET':    
    colorsinlist = []
    for color in colorData:
      if color["id"] < 1000:
      # for x in range(5):
        colorsinlist.append(color)
  return render_template('index.html', colors = colorsinlist)
  # return render_template('colorslist.html', colors = colorsinlist)

@app.route('/colorlist/<pagenum>', methods=['GET'])
def colorListDisplayAlt(pagenum=None):
  if request.method =='GET':    
    colorsinlist = []
    pageAmount = 1000
    pageSkip = int(pagenum) * 1000
    pageEnding = pageSkip + 1000

    for color in colorData:
      if color["id"] < pageEnding and color["id"] > pageSkip - 1:
        colorsinlist.append(color)
  return render_template('colorslist.html', colors = colorsinlist)

@app.route('/alphabets')
def alpha():
  letters = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z'
]

@app.route('/colors', methods=['GET'])
def colorFull():
  if request.method =='GET':    
    colorsinlist = []
    for color in colorData:
      if color["id"] < 1000:
      # for x in range(5):
        colorsinlist.append(color)
  # return "jsonify(colorsinlist)"
  return jsonify(colorsinlist)

@app.errorhandler(404)
def page_not_found(e):
  # if request.method =='GET':    
  #   colorsinlist = []
  #   for color in colorData:
  #     if color["id"] < 1000:
  #     # for x in range(5):
  #       colorsinlist.append(color)
  # # return "jsonify(colorsinlist)"
  # return jsonify(colorsinlist)
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('400.html'), 400

# 1 = 1000 - 1999
# 2 = 2000 - 1999
# limit 1000
# Skip -- Pages




@app.route('/colors/full/<pagenum>', methods=['GET'])
def colorFullpage(pagenum=None):
  if request.method =='GET':    
    colorsinlist = []
    pageAmount = 1000
    pageSkip = int(pagenum) * 1000
    pageEnding = pageSkip + 1000

    for color in colorData:
      if color["id"] < pageEnding and color["id"] > pageSkip - 1:
        colorsinlist.append(color)
  return jsonify(colorsinlist)

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