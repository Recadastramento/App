from flask import Flask, render_template, request, jsonify
from sugest import sugestoes
from preencher import autopreencher  # Importe a função autopreencher
from sugest import CadastroPIB
from flask_cors import CORS
from cep import consulta_cep

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sugestoes', methods=['GET'])
def sugestoes_route():
    return sugestoes()

@app.route('/preencher', methods=['POST'])  # Novo endpoint
def preencher_route():
    print('ok')
    nome_inserido = request.form.get('nome')  # Obtém o nome do corpo da requisição
    if not nome_inserido:
        return jsonify({"error": "Nome não informado"}), 400
    
    # Aqui você pode adicionar a lógica para confirmar o nome
    if not confirmar_nome(nome_inserido):  # Verifica se o nome é válido
        return jsonify({"error": "Nome inválido ou não encontrado"}), 404

    dados = autopreencher(nome_inserido)  # Chama a função para preencher os dados
    """ if "error" in dados:
        return jsonify(dados), 404 """
    
    return jsonify(dados)  # Retorna os dados preenchidos como JSON

def confirmar_nome(nome):
    # Verifica se o nome está na lista de nomes completos
    return nome in CadastroPIB["Nome Completo"].values  # Ajuste para a verificação correta

@app.route('/confirmar_cep', methods=['POST'])
def confirmar_cep_route():
    cep_input = request.form.get('cep')  # Obtém o CEP do corpo da requisição
    if not cep_input:
        return jsonify({"error": "CEP não informado"}), 400

    dados = consulta_cep(cep_input)  # Chama a função para consultar o CEP

    if "erro" in dados:
        return jsonify(dados), 404  # Retorna erro se o CEP não for encontrado

    return jsonify(dados)  # Retorna os dados do endereço como JSON

    


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
