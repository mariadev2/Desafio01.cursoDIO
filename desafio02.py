#variaveis

def menu(opcao_selecionada):
    opcao_selecionada = int(input('''
    ******************MENU******************
    [1]Deposito
    [2]Saque
    [3]Extrato
    [4]Sair
    [5]Criar usuário
    [6]Abrir conta
    ****************************************

    '''))
    return opcao_selecionada

def main():

    limite_vezes_permitido, limite_valor, limite_vezes =3, 500, 0
    saldo,saque,deposito,opcao_selecionada = 0, 0, 0,0
    usuarios, extrato, agencia,contas = [], "", "0001",[]

    while True:
        opcao_selecionada = menu(opcao_selecionada)

        if opcao_selecionada == 2:
                saque= float(input("Valor a ser sacado:\n"))
                saldo,extrato = realizar_saque(
                     saldo=saldo,
                     extrato=extrato,
                     saque=saque,
                     limite_valor=limite_valor,
                     limite_vezes=limite_vezes,
                     limite_vezes_permitidos=limite_vezes_permitido)
                

        elif opcao_selecionada == 1:
                deposito= float(input("Valor a ser depositado\n"))
                saldo,extrato = realizar_deposito(saldo,deposito,extrato)

        elif opcao_selecionada == 3:
                exibir_extrato(saldo,extrato=extrato)

        elif opcao_selecionada == 5:
             criar_usuario(usuarios)
             print(usuarios)
        elif opcao_selecionada==6:
             conta = len(contas) + 1
             conta = abrir_conta(agencia, conta, usuarios)
             if conta:
                contas.append(conta)
                print(contas)

        elif opcao_selecionada == 4:
                break
        else:
                print("Opção invalida\n")
                continue  
        
def criar_usuario(usuarios):
     
     cpf=str(input("Digite seu cpf:"))
     usuario= filtar(cpf,usuarios)
     if usuario:
          print("cpf cadastrado!")
          return
     else:
        nome=str(input("Digite seu nome:"))
        data_nascimento=str(input("Digiet sua Data de nascimento"))
        endereco=str(input("Digite seu enderço:"))

        usuarios.append({"nome":nome,"cpf":cpf,"data_nascimento":data_nascimento,"endereço":endereco})
        print("Usuario criado com sucesso!")

def abrir_conta (agencia,conta,usuarios):
     cpf=str(input("Digite seu cpf:"))
     usuario= filtar(cpf,usuarios)
     if usuario:
          print("conta criada com sucesso")
          return{"agencia":agencia,"conta":conta,"usuario":usuario}

def filtar(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def realizar_deposito (saldo,deposito,extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += (f"Deposito:\tR${deposito:.2f}\n") 
        print("Deposito realizado com sucesso")       
    else:
        print("Operação falhou! insira um valor acima de 0")

    return saldo,extrato

def realizar_saque(*,saldo,saque,extrato, limite_valor,limite_vezes, limite_vezes_permitidos):
    if saque > saldo:
        print("Saldo insuficiente")
    elif limite_vezes >= limite_vezes_permitidos:
        print("Voce ja ultrapassou os 3 saques, tente novamente amanhã!")
    elif saque > limite_valor:
        print("Seu saque nao deve ultrapassar R$ 500,00, tente novamente!")
    else:
        limite_vezes += 1
        saldo -= saque
        extrato+= (f"Saque:\tR$ {saque:.2f}\n") 
    print(f"Foram realizados {limite_vezes} Saques\n")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print('=====================EXTRATO=====================')
    print("Nao foram realizadas nenhuma transação" if not extrato else extrato)
    print(f"Seu saldo é:\t{saldo:.2f}")
    print("===================================================")

main()

#funcionamento
