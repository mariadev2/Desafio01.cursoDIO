lista_deposito = []
lista_saque = []
saldo = 0
deposito =0
limite_saque_vezes_cont = 0
limite_saque = 500
limite_saque_vezes = 3

menu = f'''SELECIONE UMA OPÇÃO NO MENU:
           [1]Extrato
           [2]Deposito
           [3]Saque
           [4]Sair
           '''

while True:
    print(menu)
    opcao = int(input("Qual opção desejada?\n"))

    if opcao == 1:
        saldo_anterior = deposito
        print(f"Extrato\n Seus depositos anteriores foi R$ {lista_deposito}\nSeus sques anteriores foi R$ {lista_saque}\nseu saldo é R$ {saldo:.2f}")
    elif opcao == 2:
            deposito = int(input("seu deposito:"))
            lista_deposito.append(deposito)
            saldo += deposito
            print(f"\nSeu saldo atual é {saldo}\n")
            

    elif opcao == 3:
         if limite_saque_vezes_cont <= limite_saque_vezes:
            saque = int(input("Qual valor do saque"))
            if saque <= saldo or saque < limite_saque:
                lista_saque.append(saque)
                saldo -= saque
                limite_saque_vezes_cont += 1
                print(f"\nSeu saldo atual é {saldo}\n")
            if saque > saldo:
                print("Saldo insuficiente")
         if limite_saque_vezes_cont > limite_saque_vezes:
             print("Ja ultrapassou 3 saques")
    elif opcao== 4:
        print("operação finalizada!")
        break


