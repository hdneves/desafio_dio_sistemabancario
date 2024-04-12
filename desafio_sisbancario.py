from time import sleep
from datetime import datetime
import pandas as pd
from pprint import pprint

def deposito():
    vl_deposito = int(input("Insiria o valor a ser depositado: "))
    print(f'Valor depositado: R${vl_deposito}')
    
    return vl_deposito


def saque(vl_deposito, saques_realizados):
    if saques_realizados >= 3:
        return False, vl_deposito, 0 

    vl_saque = int(input(f'Saque: R$'))
    if vl_saque > vl_deposito or vl_saque > 500 or vl_saque <= 0:
        print('''Verifique se o valor inserido esteja nas condições:\n1) Saldo suficiente;\n2) Limite de saque diário: R$500;\n3) Valores diferentes de zero;''')
        return True, vl_deposito, 0  

    vl_deposito -= vl_saque
    saques_realizados += 1
    print(f'Saques realizados: {saques_realizados}')
    return True, vl_deposito, vl_saque  

def tituloSistema():
    frase = '𝐇 𝐃  𝐁 𝐀 𝐍 𝐊'
    print('')
    print('⤳'*len(frase))
    print(frase)
    print('⤳'*len(frase))
    print('')
    
saldo = 0
limite = 0
saques_realizados = 0

extrato = {}
while True:
    
    tituloSistema()
    print('𝐒 𝐄 𝐋 𝐄 𝐂 𝐈 𝐎 𝐍 𝐄  𝐀  𝐎 𝐏 𝐄 𝐑 𝐀 𝐂̧ 𝐀̃ 𝐎 \n\n1-Verificar Saldo | 2-Extrato | 3-Depósito | 4-Saque | 9-Sair')
    operacao = int(input('> '))

    if operacao == 9:
        break

    if operacao == 1:
        print(f'Saldo Atual: R${saldo},00')

    if operacao == 2: #exibir extrato
        df = pd.DataFrame(list(extrato.items()), columns=['Data', 'Valor'])
        df['Modalidade'] = df['Data'].str.split(' - ').str[-1]
        df['Valor'] = df['Valor'].replace({'[R$,]': ''}, regex=True).astype(float)
        total_acao = df['Valor'].sum()
        df_total = pd.DataFrame({'Data': ['Total'], 'Valor': [f'R${total_acao:.2f}'], 'Modalidade': ['']})

        df = pd.concat([df, df_total], ignore_index=True)
        df['Data'] = df['Data'].apply(lambda x: x.split(' -')[0])
        pprint(df)
    if operacao == 3:
        vl_deposito = deposito()
        saldo += vl_deposito

        chave_extrato = datetime.now().strftime("%d/%m/%Y %H:%M:%S - DEPÓSITO")
        extrato[chave_extrato] = f'+R${vl_deposito}'
        continue
    
    if operacao == 4:
        continuar, saldo, vl_saque = saque(saldo, saques_realizados)
        if not continuar:  # Se o limite de saques foi atingido
            print("Limite de saques diários atingido.")
            sleep(1)
            continue
            
        saques_realizados += 1
        chave_extrato = datetime.now().strftime("%d/%m/%Y %H:%M:%S - SAQUE")
        extrato[chave_extrato] = f'-R${vl_saque}'

