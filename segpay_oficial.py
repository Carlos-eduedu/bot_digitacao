from segpay_funcs import digitacao
from datetime import datetime
import time
import pandas as pd
import PySimpleGUI as pg
import random

tool = digitacao(1,1)
base = pg.popup_get_file('insira a base de dados')
resp_iniciar = tool.iniciar()
aprovados  = 0
reprovados = 0
total = 0
login = str(input('insira o login de acesso a plataforma: '))
senha = str(input('insira a senha de acesso a plataforma: '))

#inicar e fazer login
if resp_iniciar == True:
    resp_login = tool.login_seg(login=login, senha=senha)
    if resp_login == True:
        tool.operacao()
        print('login executado com secesso')
    else:
        print('erro ao fazer login')
else:
    print('Erro ao iniciar')

#digitacao
base1 = pd.read_excel(base)
base_livre = base1[(base1['STATUS'].isnull())]
for i,linha in base_livre.iterrows():
    nome        = str(base1.loc[i,'NOME'])
    nomes       = nome.split()
    name        =  (f'{nomes[0]} {nomes[-1]}')
    nascimento  = str(base1.loc[i,'NASCIMENTO'])
    sexo        = str(base1.loc[i,'SEXO'])
    cpf         = str(base1.loc[i,'CPF'])
    email       = str(base1.loc[i,'EMAIL'])
    telefone    = str(base1.loc[i,'TELEFONE'])
    cep         = str(base1.loc[i,'CEP'])
    endereco    = str(base1.loc[i,'ENDERECO'])
    num         = str(base1.loc[i,'N'])
    bairro      = str(base1.loc[i,'BAIRRO'])
    cidade      = str(base1.loc[i,'CIDADE'])
    uf          = str(base1.loc[i,'UF'])
    card_number = str(base1.loc[i,'CARD_NUMBER'])
    card        = card_number[1:18]
    mes         = str(base1.loc[i,'MES'])
    ano         = str(base1.loc[i,'ANO'])
    mes_num     = len(mes)
    if mes_num == 1:
        mes = (f'0{mes}')
    else:
        mes = mes
    vencimento = (f'{mes}{ano}')

    #dados de tempo / calculo intervalo de tempo
    time_3 = time.strftime('%H:%M:%S')
    tempo = random.randint(1,10)
    tool.limpar()
    
    #campos de informacoes do cliente
    time.sleep(tempo)
    tool.preenche_str(element='//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[1]/div/div/div/input',info=name)
    tool.preenche_int(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[1]/div[2]/div/div/div/input',info=nascimento)
    tool.preenche_sexo(sexo)
    tool.preenche_int(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[1]/div/input',info=cpf)
    tool.preenche_str(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[2]/div/div/div/input', info=email)
    tool.preenche_int(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[1]/div[2]/div[3]/div/input',info=telefone)

    #campos de informacoes de endereco
    time.sleep(tempo)
    tool.preenche_int(element='//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div[1]/div/input',info=cep)
    tool.preenche_str(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div[2]/div/div/div/input', info=endereco)
    tool.preenche_int(element='//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[2]/div[1]/div[3]/div/div/div/input',info=num)
    tool.preenche_str(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div[2]/div/div/div/input',info=bairro)
    tool.preenche_str(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div[3]/div/div/div/input',info=cidade)
    tool.preenche_str(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/div[4]/div/div/div/input',info=uf)

    #campos de informcoes de cartao
    time.sleep(tempo)
    tool.preenche_int(element='/html/body/div/div/div/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/input',info=card_number)
    tool.preenche_int(element='//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/div[3]/input',info=vencimento)

    tool.clicar_campo(element='//*[@id="root"]/div/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div/button')
    var = tool.inserir()

    #tratamento do resultado da digitacao
    if var == True:
        print('REPROVADO')
        base1.loc[i,'STATUS'] = 'REPROVADO'
        total += 1
        reprovados += 1 
        base1.to_excel(base)
        tool.limpar()
    else:
        print('APROVADO')
        base1.loc[i,'STATUS'] = 'APROVADO'
        total += 1
        aprovados += 1 
        base1.to_excel(base)
        tool.limpar()

    time_4 = time.strftime('%H:%M:%S')
    time_1 = datetime.strptime(time_3,"%H:%M:%S")
    time_2 = datetime.strptime(time_4,"%H:%M:%S")

    time_interval = time_2 - time_1
    print(time_interval)

    #tela de resultados
    print('+--------------+')
    print(f'|total:{total}       |')
    print(f'|aprovados:{aprovados}   |')
    print(f'|reprovados:{reprovados}  |')
    print('+--------------+')

#calculo de aproveitamento de base
try:
    aproveitamento = (aprovados / total)
    print(f'aproveitamento foi de {aproveitamento:.2%}')
except:
    print('erro ao calcular o aproveitamento')
sair = str(input('Deseja sair (Y/N): '))
