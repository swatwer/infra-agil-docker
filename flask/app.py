from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify({'status' : 'Rodando!'})

app.run(host='0.0.0.0.')

