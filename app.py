from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from sugest import sugestoes
from preencher import autopreencher  # Importe a função autopreencher
from sugest import CadastroPIB
from subirgoogle import confirmando  # Importa a função confirmando
from flask_cors import CORS
from cep import consulta_cep
from foto import upload_to_drive
import os
from Dados import link_foto

app = Flask(__name__)
app.secret_key = "key"
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

    # Chama a função autopreencher
    dados = autopreencher(nome_inserido)

    # Chama a função confirmando
    confirmando(None)  # Chame a função confirmando

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
def finalizar_cadastro_route():
    confirmando()  # Chama a função confirmando()
    return jsonify({"message": "Cadastro finalizado com sucesso!"})

@app.route('/upload', methods=['POST'])
def upload():
    global link_foto
    if 'file' not in request.files:
        flash('Nenhum arquivo enviado.')
        return redirect(url_for('index'))
    
    file = request.files['file']

    if file.filename == '':
        flash('Nenhum arquivo selecionado.')
        return redirect(url_for('index'))
    
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    
    try:
        link = upload_to_drive(file_path)
        link_foto.value = link
        print(link_foto.value)
    except Exception as e:
        print(f'Erro ao fazer upload para o Google Drive: {e}')  # Log de erro
        flash(f'Erro ao fazer upload para o Google Drive: {e}')
        return redirect(url_for('index'))

    
    flash(f'Upload realizado com sucesso! Link: {link}')
    return redirect(url_for('index'))  # Redireciona para a página inicial


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
