from flask import Flask, send_file
import os
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)
CadastroPIB = pd.DataFrame() 

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRET_FILE = "Versão PARA Site\\tokens\\credentials.json"

Dtoken = "Versão PARA Site\\tokens\\Dtoken.json"

@app.route('/download_csv', methods=['GET'])
def download_csv():
    global CadastroPIB
    if os.path.exists(Dtoken):
        creds = Credentials.from_authorized_user_file(Dtoken, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(Dtoken, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    file_id = '1WtuPyPqtV0gZnnoPhLZLY1qfmgPNAv9vQDqK4NV6LQo'
    request = service.files().export_media(fileId=file_id, mimeType='text/csv')
    file_content = request.execute()

    with open('arquivo.csv', 'wb') as f:
        f.write(file_content)

    # Carregar o arquivo CSV em um DataFrame
    CadastroPIB = pd.read_csv('arquivo.csv')
    for item in CadastroPIB:
        print(item)

   # return send_file('arquivo.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
