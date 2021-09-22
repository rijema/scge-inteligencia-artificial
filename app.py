from flask import Flask, jsonify,json

app  = Flask(__name__)

arquivo = open('saida.json','r')
jsondata=arquivo.read()

lendo=json.loads(jsondata)


@app.route('/')

def home():
    
    return jsonify(lendo),200

if(__name__ == '__main__'):
    app.run(debug=True)

# print("Be careful not to fall off!");