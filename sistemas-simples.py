menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo_atual = 0.0
limite_saque = 500.0
extrato = ""
qtd_saques = 0
MAX_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor para depósito: "))

        if valor_deposito > 0:
            saldo_atual += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Não foi possível realizar o depósito. Valor inválido.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor para saque: "))

        saldo_insuficiente = valor_saque > saldo_atual
        acima_limite = valor_saque > limite_saque
        excedeu_quantidade_saques = qtd_saques >= MAX_SAQUES

        if saldo_insuficiente:
            print("Saque não realizado! Saldo insuficiente.")

        elif acima_limite:
            print("Saque não realizado! Valor informado ultrapassa o limite permitido.")

        elif excedeu_quantidade_saques:
            print("Saque não realizado! Quantidade máxima de saques atingida.")

        elif valor_saque > 0:
            saldo_atual -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            qtd_saques += 1
        else:
            print("Saque não realizado! Valor inválido.")

    elif opcao == "3":
        print("\n============= EXTRATO =============")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo_atual:.2f}")
        print("===================================")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")