# Crie um algoritmo que controle as movimetações de bolsas de sangue do
# O programa deve ter as seguintes opções:

# - Doar sangue (define qual tipo e acrescente 1 unidade)
# - Retirar sangue (define qual tipo e retira múltiplos de 5 unidades)
# - Visualizar saldo de bolsas
# - Consultar movimentações de estoque

tipos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
saldos = [10, 10, 12, 11, 6, 6, 2, 1]
movimentacoes_qtde = []
movimentacoes_tipo = []

while True:
    print("[1] Doar sangue\n[2] Retirar sangue\n[3] Visualizar saldo\n[4] Consultar movimetações\n[5] Sair")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        tipo = input("Informe o tipo de sangue para doar: ")
        qtde = int(input("Informe a quantidade para doar: "))
        if tipo in tipos:
            saldos[tipos.index(tipo)] += qtde
            movimentacoes_tipo.append(tipo)
            movimentacoes_qtde.append("+" + str(qtde))
        else:
            print("Tipo de sangue inválido")

    if opcao == 2:
        tipo = input("Informe o tipo de sangue para retirar: ")
        qtde = int(input("Informe a quantidade para retirar (5x): "))
        if tipo in tipos:
            if saldos[tipos.index(tipo)] >= qtde * 5:
                saldos[tipos.index(tipo)] -= qtde * 5
                movimentacoes_tipo.append(tipo)
                movimentacoes_qtde.append(-(qtde * 5))
            else:
                print("Quantidade em estoque insuficiente")
        else:
            print("Tipo de sangue inválido")

    if opcao == 3:
        for i in range(len(tipos)):
            print(f"Tipo: {tipos[i]} \t Estoque: {saldos[i]}")

    if opcao == 4:
        for i in range(len(movimentacoes_tipo)):
            print(f"{movimentacoes_tipo[i]} \t : {movimentacoes_qtde[i]}")

    if opcao == 5:
        break

    if 0 >= opcao or opcao > 5:
        print("Opção inválida")
