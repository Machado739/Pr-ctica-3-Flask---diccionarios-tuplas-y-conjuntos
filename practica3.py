from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/agregar_clave_valor/<string:clave>/<string:valor>', methods=['POST'])
def agregar_clave_valor(clave, valor):
    diccionario = request.json
    diccionario[clave] = valor
    return jsonify(diccionario)

@app.route('/eliminar_clave_valor/<string:clave>', methods=['DELETE'])
def eliminar_clave_valor(clave):
    diccionario = request.json
    if clave in diccionario:
        del diccionario[clave]
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404

@app.route('/modificar_valor/<string:clave>/<string:nuevo_valor>', methods=['PUT'])
def modificar_valor(clave, nuevo_valor):
    diccionario = request.json
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return jsonify(diccionario)
    else:
        return 'La clave no existe en el diccionario', 404

@app.route('/combinar_diccionarios', methods=['POST'])
def combinar_diccionarios():
    diccionario1 = request.json
    diccionario2 = request.args.get('diccionario2')
    diccionario2 = json.loads(diccionario2)
    diccionario1.update(diccionario2)
    return jsonify(diccionario1)


@app.route('/agregar_elemento_conjunto/<string:elemento>', methods=['POST'])
def agregar_elemento_conjunto(elemento):
    conjunto = request.json
    conjunto.add(elemento)
    return jsonify(list(conjunto))


@app.route('/eliminar_elemento_conjunto/<string:elemento>', methods=['DELETE'])
def eliminar_elemento_conjunto(elemento):
    conjunto = request.json
    if elemento in conjunto:
        conjunto.remove(elemento)
        return jsonify(list(conjunto))
    else:
        return 'El elemento no existe en el conjunto', 404

@app.route('/combinar_conjuntos', methods=['POST'])
def combinar_conjuntos():
    conjunto1 = request.json
    conjunto2 = request.args.get('conjunto2')
    conjunto2 = json.loads(conjunto2)
    conjunto_resultante = conjunto1.union(conjunto2)
    return jsonify(list(conjunto_resultante))

@app.route('/diferencia_entre_conjuntos', methods=['POST'])
def diferencia_entre_conjuntos():
    conjunto1 = request.json
    conjunto2 = request.args.get('conjunto2')
    conjunto2 = json.loads(conjunto2)
    diferencia = conjunto1.difference(conjunto2)
    return jsonify(list(diferencia))

@app.route('/agregar_elemento_tupla/<string:elemento>', methods=['POST'])
def agregar_elemento_tupla(elemento):
    tupla = tuple(request.json)
    nueva_tupla = tupla + (elemento,)
    return jsonify(list(nueva_tupla))

@app.route('/eliminar_elemento_tupla/<string:elemento>', methods=['DELETE'])
def eliminar_elemento_tupla(elemento):
    tupla = tuple(request.json)
    if elemento in tupla:
        nueva_tupla = tuple(e for e in tupla if e != elemento)
        return jsonify(list(nueva_tupla))
    else:
        return 'El elemento no existe en la tupla', 404

@app.route('/concatenar_tuplas', methods=['POST'])
def concatenar_tuplas():
    tupla1 = tuple(request.json)
    tupla2 = request.args.get('tupla2')
    tupla2 = json.loads(tupla2)
    nueva_tupla = tupla1 + tupla2
    return jsonify(list(nueva_tupla))

@app.route('/revertir_tupla', methods=['POST'])
def revertir_tupla():
    tupla = tuple(request.json)
    nueva_tupla = tuple(reversed(tupla))
    return jsonify(list(nueva_tupla))

if __name__ == "__main__":
    app.run()
