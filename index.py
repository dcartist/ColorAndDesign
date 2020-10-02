from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def index():
    return "Colors"
app.run(port=3000, debug=True)