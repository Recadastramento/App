from sugest import CadastroPIB
from Dados import( 
        matricula, nomecompleto,
        cpf, datanascimento, tipo_sanguineo, 
        estado_civil, datacasamento, profissao, 
        naturalidade, nacionalidade,rua, complemento,
        bairro, municipio, estado, cep, tel_residencial,
        tel_celular, email, nome_pai,
        nome_mae, nome_conjuge,
        datanascimento_conjuge,
        cargo_atual, databatismo, igrejabatismo,
        entradaPIB, formaentrada
)
def autopreencher(nome_inserido):
    if (CadastroPIB["Nome Completo"] == nome_inserido).any():
        indice = CadastroPIB[CadastroPIB["Nome Completo"] == nome_inserido].index[0]
        nomecompleto.value = CadastroPIB["Nome Completo"].iloc[indice]
        matricula.value = CadastroPIB["Matrícula"].iloc[indice]
        cpf.value = CadastroPIB["CPF"].iloc[indice]
        datanascimento.value = CadastroPIB["Data de Nascimento"].iloc[indice]
        tipo_sanguineo.value = CadastroPIB["Tipo Sanguíneo"].iloc[indice]
        estado_civil.value = CadastroPIB["Estado Civil"].iloc[indice]
        datacasamento.value = CadastroPIB["Data de Casamento"].iloc[indice]
        profissao.value = CadastroPIB["Profissão"].iloc[indice]
        naturalidade.value = CadastroPIB["Naturalidade"].iloc[indice]
        nacionalidade.value = CadastroPIB["Nacionalidade"].iloc[indice]
        rua.value = CadastroPIB["Rua"].iloc[indice]
        complemento.value = CadastroPIB["Complemento"].iloc[indice]
        bairro.value = CadastroPIB["Bairro"].iloc[indice]
        municipio.value = CadastroPIB["Cidade"].iloc[indice]
        estado.value = CadastroPIB["Estado"].iloc[indice]
        cep.value = CadastroPIB["CEP"].iloc[indice]
        tel_residencial.value = CadastroPIB["Tel. Residencial"].iloc[indice]
        tel_celular.value = CadastroPIB["Celular"].iloc[indice]
        email.value = CadastroPIB["e-mail"].iloc[indice]
        nome_pai.value = CadastroPIB["Nome do Pai"].iloc[indice]
        nome_mae.value = CadastroPIB["Nome da Mãe"].iloc[indice]
        nome_conjuge.value = CadastroPIB["Nome"].iloc[indice]
        datanascimento_conjuge.value = CadastroPIB["Nascimento"].iloc[indice]
        cargo_atual.value = CadastroPIB["Cargo Atual"].iloc[indice]
        databatismo.value = CadastroPIB["Databatismo"].iloc[indice]
        igrejabatismo.value = CadastroPIB["Igreja"].iloc[indice]
        entradaPIB.value = CadastroPIB["Data Membro"].iloc[indice]
        formaentrada.value = CadastroPIB["Modo"].iloc[indice]    

        print("Teste")
        print(matricula.value)
        print(nomecompleto.value)