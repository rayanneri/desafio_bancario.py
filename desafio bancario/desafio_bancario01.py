menu = """

         S E J A  B E M  V I N D O (A)  A O  B A N C O  R A Y!\n
        Selecione a opção desejado no teclado númerico do caixa.

                (1) depositar
                (2) sacar
                (3) extrato
                (0) sair

                => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou! O valor informado é inválido") 
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor inserido é inválido.")

        else:
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "3":
        print("********EXTRATO********")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Movimentação realizada:\n" + (extrato if extrato else "Não foram realizadas movimentações."))
        print("************************")

    elif opcao == "0":
            break
