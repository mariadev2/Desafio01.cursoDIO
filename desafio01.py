lista_deposito = []
lista_saque = []
saldo = 0
deposito =0
limite_saque_vezes_cont = 0
limite_saque = 500
limite_saque_vezes = 3
saque = 0
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
<<<<<<< HEAD
        print("")
        print("#"*50)
        print("EXTRATO")
        print(f"\nSeus depositos anteriores foram R$ {lista_deposito}\n" if deposito > 0 else "sem deposito")
        print(f"Seus saques anteriores foi R$ {lista_saque}\n"if saque > 0 else "Sem saques anteriores")
        print(f"seu saldo é R$ {saldo:.2f}")
        print("#"*50)
=======
        saldo_anterior = deposito
        print(f"Extrato\n Seus depositos anteriores foi R$ {lista_deposito}\nSeus saques anteriores foi R$ {lista_saque}\nseu saldo é R$ {saldo:.2f}")
    elif opcao == 2:
            deposito = int(input("seu deposito:"))
            lista_deposito.append(deposito)
            saldo += deposito
            print(f"\nSeu saldo atual é {saldo}\n")
            
>>>>>>> c783c532d9717e48bd3cd249da74fd4d81262ba7

    elif opcao == 2:
            deposito = int(input("seu deposito:\n"))
            if deposito < 0:
                print("insira um valor acima de 0")
            else:
                lista_deposito.append(deposito)
                saldo += deposito
                print(f"\nSeu saldo atual é {saldo}\n")
  
    elif opcao == 3:
        saque = int(input("Qual valor do saque\n"))
        if limite_saque_vezes_cont >= 3:
            print("Ultrapassou 3x")
        elif saque > saldo:
            print("Seu saque ultrapassou valor disponivel")
        elif saque > limite_saque:
            print("ultrapassou limite de saque")
        else:
            lista_saque.append(saque)
            saldo -= saque
            limite_saque_vezes_cont += 1
            print(f"\nSeu saldo atual é {saldo}\nVOCE TEM {limite_saque_vezes_cont} LIMITES PARA SACAR")

    elif opcao== 4:
        print("operação finalizada!")
        break
    else: 
        print("insira uma opção valida!")


