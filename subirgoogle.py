import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Dados import (link_foto, matricula, nomecompleto, cpf,
        datanascimento, sexo, tipo_sanguineo, 
        estado_civil, datacasamento, profissao, 
        naturalidade, nacionalidade,rua, complemento,
        bairro, municipio, estado, cep, tel_residencial,
        tel_celular, email, nome_pai, pai_membro,
        nome_mae, mae_membro, nome_conjuge,
        datanascimento_conjuge, conjuge_membro,
        cargo_atual, databatismo, igrejabatismo,bairro_igreja,
        entradaPIB, formaentrada, 
        nome_filho1, datanascimento_filho1, filho1_membro, 
        nome_filho2, datanascimento_filho2, filho2_membro,
        nome_filho3, datanascimento_filho3, filho3_membro,
        nome_filho4, datanascimento_filho4, filho4_membro,
        nome_filho5, datanascimento_filho5, filho5_membro, cadastrador )

def confirmando():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    SPREADSHEET_ID = "197dGyWjtAVUVR2K8eODfIxfrEFgeErTcxMhp3OIX8N0"
    RANGE_NAME = "Dados!A1:AY3000"

    creds = None
    Stoken = "Versão PARA Site\\tokens\\Stoken.json"

    if os.path.exists(Stoken):
        creds = Credentials.from_authorized_user_file(Stoken, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("Versão PARA Site\\tokens\\credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open(Stoken, "w") as token:
            token.write(creds.to_json())
    print("Autenticação concluída.")
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        dados = {
                "Foto": [str(link_foto.value)],
                "Nome Completo": [nomecompleto.value],
                "Matrícula": [str(matricula.value)], 
                "CPF": [str(cpf.value)], 
                "Data de Nascimento": [str(datanascimento.value)],  
                "Sexo": [str(sexo.value)],  
                "Tipo Sanguíneo": [str(tipo_sanguineo.value)],  
                "Estado Civil": [str(estado_civil.value)],  
                "Data de Casamento": [str(datacasamento.value)],  
                "Profissão": [str(profissao.value)],  
                "Naturalidade": [str(naturalidade.value)], 
                "Nacionalidade": [str(nacionalidade.value)], 
                "Rua": [str(rua.value)], 
                "Complemento": [str(complemento.value)],  
                "Bairro": [str(bairro.value)], 
                "Município": [str(municipio.value)],  
                "Estado": [str(estado.value)],  
                "CEP": [str(cep.value)],  
                "Tel. Residencial": [str(tel_residencial.value)],  
                "Tel. Celular": [str(tel_celular.value)],  
                "E-mail": [str(email.value)],  
                "Nome do Pai": [str(nome_pai.value)],  
                "Pai Membro": [str(pai_membro.value)],
                "Nome da Mãe": [str(nome_mae.value)], 
                "Mãe Membro": [str(mae_membro.value)],
                "Nome do Conjuge": [str(nome_conjuge.value)],
                "Data de Nascimento Conjuge": [str(datanascimento_conjuge.value)],
                "Conjuge Membro": [str(conjuge_membro.value)],
                "Cargo atual": [str(cargo_atual.value)],
                "Data Batismo": [str(databatismo.value)],
                "Bairro Igreja Batismo":[str(bairro_igreja)],
                "Igreja Batismo": [str(igrejabatismo.value)],
                "Data de Entrada PIB": [str(entradaPIB.value)],
                "Forma de entrada": [str(formaentrada.value)],
                "Nome do filho(a) 1": [str(nome_filho1.value)],
                "Data de Nascimento do filho(a) 1": [str(datanascimento_filho1.value)],
                "Seu filho(a) 1 é membro da PIB Pavuna?": [str(filho1_membro.value)],
                "Nome do filho(a) 2": [str(nome_filho2.value)],
                "Data de Nascimento do filho(a) 2": [str(datanascimento_filho2.value)],
                "Seu filho(a) 2 é membro da PIB Pavuna?": [str(filho2_membro.value)],
                "Nome do filho(a) 3": [str(nome_filho3.value)],
                "Data de Nascimento do filho(a) 3": [str(datanascimento_filho3.value)],
                "Seu filho(a) 3 é membro da PIB Pavuna?": [str(filho3_membro.value)],
                "Nome do filho(a) 4": [str(nome_filho4.value)],
                "Data de Nascimento do filho(a) 4": [str(datanascimento_filho4.value)],
                "Seu filho(a) 4 é membro da PIB Pavuna?": [str(filho4_membro.value)],
                "Nome do filho(a) 5": [str(nome_filho5.value)],
                "Data de Nascimento do filho(a) 5": [str(datanascimento_filho5.value)],
                "Seu filho(a) 5 é membro da PIB Pavuna?": [str(filho5_membro.value)],
                "Cadastrante": [(str(cadastrador.value))]
        }

        valores = [[v[0] for v in dados.values()]]
        print("Valores a serem adicionados:", valores)

        request = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": valores},
        )
        response = request.execute()

        print(f"Dados adicionados com sucesso: {response}")
        print("Dados adicionados com sucesso.")
    except HttpError as error:
        print(f"Erro ao adicionar dados: {error}")
