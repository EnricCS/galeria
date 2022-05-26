from flask import Flask, render_template, request, redirect
from bson import ObjectId
from pymongo import MongoClient

def comprueba_fondo():
	pass

DOCUMENTOS = ['doc', 'docx']

def usuario():
	pass

def password():
	pass

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
basedatos = client.fondos
misfondos = basedatos.lista

@app.route('/')
@app.route('/aportar', methods = ['POST'])
def agregar():
    
    tit = request.values.get('titulo')
    desc = request.values.get('descripcion')
    tags = []
    lista=['animales','naturaleza', 'ciudad', 'deporte', 'personas']
    for tema in lista:
        if request.values.get(tema):
            tags += tema
    misfondos.insert({'título': tit, 'descripción': desc, 'tags': tags})
    return redirect('/insertar')

@app.route('/insertar', methods = ['POST'])
if __name__ == '__main__':
    app.run()