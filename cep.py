import requests
from Dados import rua, bairro, municipio, estado  # Certifique-se de que estas são variáveis globais

def consulta_cep(cep):
    cep = cep.replace("-", "").replace(".", "").strip()

    if not cep.isdigit() or len(cep) != 8:
        return {"erro": "Formato de CEP inválido."}

    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            return {"erro": "CEP não encontrado."}

        # Atualiza os valores
        rua.value = dados['logradouro']
        bairro.value = dados['bairro']
        municipio.value = dados['localidade']
        estado.value = dados['uf']

        print(rua.value)
        print(bairro.value)
        print(municipio.value)
        print(estado.value)

        return dados
    else:
        return {"erro": "Erro na consulta."}
