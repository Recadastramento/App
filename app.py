from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from sugest import sugestoes
from preencher import autopreencher
from sugest import CadastroPIB
from subirgoogle import confirmando
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

@app.route('/preencher', methods=['POST'])
def preencher_route():
    nome_inserido = request.form.get('nome')
    if not nome_inserido:
        return jsonify({"error": "Nome não informado"}), 400
    
    if not confirmar_nome(nome_inserido):
        return jsonify({"error": "Nome inválido ou não encontrado"}), 404

    dados = autopreencher(nome_inserido)
    return jsonify(dados)

def confirmar_nome(nome):
    return nome in CadastroPIB["Nome Completo"].values

@app.route('/confirmar_cep', methods=['POST'])
def confirmar_cep_route():
    cep_input = request.form.get('cep')
    if not cep_input:
        return jsonify({"error": "CEP não informado"}), 400

    dados = consulta_cep(cep_input)
    if "erro" in dados:
        return jsonify(dados), 404

    return jsonify(dados)

@app.route('/finalizarCadastro', methods=['POST'])
def finalizar_cadastro_route():
    try:
        confirmando()
        flash("Cadastro finalizado com sucesso!")  # Mensagem de sucesso
        return redirect(url_for('index'))
    except Exception as e:
        print(f'Erro ao finalizar cadastro: {e}')
        flash("Erro ao finalizar cadastro.")  # Mensagem de erro
        return redirect(url_for('index'))

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
    except Exception as e:
        print(f'Erro ao fazer upload para o Google Drive: {e}')
        flash(f'Erro ao fazer upload para o Google Drive: {e}')
        return redirect(url_for('index'))

    flash(f'Upload realizado com sucesso! Link: {link}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
