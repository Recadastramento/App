from flask import request, jsonify
from Dadosgoogledrive import download_csv

download_csv()
from Dadosgoogledrive import CadastroPIB
nomes_completos = CadastroPIB["Nome Completo"].tolist()

def sugestoes():
    texto_digitado = request.args.get('texto', '')
    sugestoes_filtradas = [
        nome for nome in nomes_completos if nome.lower().startswith(texto_digitado.lower())
    ]
    return jsonify(sugestoes=sugestoes_filtradas)