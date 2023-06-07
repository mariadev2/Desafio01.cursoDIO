#variaveis
limite_vezes_permitido, limite_valor, limite_vezes =3, 500, 0
saldo,saque,deposito = 0, 0, 0
extrato_saque, extrato_deposito = [], []
#funções


def realizar_deposito (*, deposito):
    global saldo
    if deposito > 0:
        saldo += deposito
        extrato_deposito.append(deposito)   
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
        extrato_saque.append(saque)   
    return saldo

#funcionamento
while True:
    print(f"Seu saldo atual é {saldo} \n")
    opcao_selecionada = int(input("MENU\n[1]Deposito\n[2]Saque\n[3]Extrato\n[4]Sair\n"))

    if opcao_selecionada == 2:
        saldo = realizar_saque(saque = int(input("Valor a ser sacado\n")))
        print(f"Foram realizados {limite_vezes} Saques\n")

    elif opcao_selecionada == 1:
        saldo = realizar_deposito(deposito= int(input("Valor a ser depositado\n")))

    elif opcao_selecionada == 3:
        print("EXTRATO\n")
        print("Saques")
        for indice, elemento in enumerate(extrato_saque):
            print(f"{indice} . R$ {elemento}\n")
        print("Depositos")
        for indice, elemento in enumerate(extrato_deposito):
            print(f"{indice} . R$ {elemento}\n")

    elif opcao_selecionada == 4:
        break
    else:
        print("Opção invalida\n")
        continue
        