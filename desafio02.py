#variaveis
limite_vezes=0
limite_vezes_permitido =3 
limite_valor =500
saldo = 0
saque = 0
deposito = 0
extrato_saque = []
extrato_deposito = []
#funções
def Cadastrar_usuario():
def abrir_conta():
def realizar_deposito (*, deposito):
    global saldo
    if deposito > 0:
        saldo += deposito
        return saldo
    else:
        print("insira um valor acima de 0")

def realizar_saque(*,saque):
    global limite_vezes, limite_valor, saldo
    if saque > saldo:
        print("Saldo insuficiente")
    elif limite_vezes >= 3:
        print("Voce ja ultrapassou os 3 saques, tente novamente amanhã!")
    elif saque > limite_valor:
        print("Seu saque nao deve ultrapassar R$ 500,00, tente novamente!")
    else:
        limite_vezes += 1
        saldo -= saque
    return saldo

def exibir_extrato(saque, deposito, extrato_saque, extrato_deposito):
    extrato_saque = extrato_saque.append(saque)
    extrato_deposito = extrato_deposito.append(deposito)
    return extrato_saque, extrato_deposito

#funcionamento
while True:
    print(f"Seu saldo atual é {saldo} \n")
    opcao_selecionada = int(input("MENU\n[1]Deposito\n[2]Saque\n[3]Extrato\n"))
    if opcao_selecionada == 2:
        saldo = realizar_saque(saque = int(input("Valor a ser sacado\n")))
        print(f"{limite_vezes} Saque\n")
    elif opcao_selecionada == 1:
        saldo = realizar_deposito(deposito= int(input("Valor a ser depositado\n")))
    elif opcao_selecionada == 3:
        extrato_saque = exibir_extrato(extrato_saque,extrato_deposito)
        extrato_deposito = exibir_extrato(extrato_deposito, extrato_saque)
        print(f"{extrato_deposito} {extrato_saque}")
    else:
        break
        