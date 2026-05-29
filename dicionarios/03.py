from datetime import datetime

estoque = {'A+': 10,
           'A-': 11,
           'B+': 12,
           'B-': 13,
           'AB+': 14,
           'AB-': 15,
           'O+': 16,
           'O-': 17}

movimentacoes = []

menu = '''
[1] Doar sangue
[2] Retirar sangue
[3] Consultar estoque
[4] Consultar movimentações
[5] Sair
'''

nome = input('Informe seu nome: ')
while True:
    print(menu)
    opcao = int(input("Opção: "))

    if opcao == 1:
        tipo = input("Informe o tipo sanguíneo para doar: ").upper()
        if tipo in estoque.keys():
            estoque[tipo] += 1

            movimento = {'Tipo': tipo,
                         'Valor': 1,
                         'Situação': 'Doação',
                         'Nome': nome,
                         'Data/Hora': datetime.now().strftime('%Y/%m/%d %H:%M')}
            movimentacoes.append(movimento)

    if opcao == 2:
        tipo = input("Informe o tipo sanguíneo para retirar: ").upper()
        if tipo in estoque.keys():
            quantidade = int(input("Informe a quantidade: "))
            if estoque[tipo] >= quantidade:
                if quantidade % 5 == 0:
                    estoque[tipo] -= quantidade
                    movimento = {'Tipo': tipo,
                                 'Valor': quantidade,
                                 'Situação': 'Retirada',
                                 'Nome': nome,
                                 'Data/Hora': datetime.now().strftime('%Y/%m/%d %H:%M')}
                    movimentacoes.append(movimento)
                else:
                    print("Quantidade precisa ser múltipla de 5")
            else:
                print("Quantidade em estoque inferior ao solicitado")


    if opcao == 3:
        print('ESTOQUE'.center(20, '-'))
        for chave, valor in estoque.items():
            print(chave.center(10), str(valor).center(10))
        print('-'*20)

    if opcao == 4:
        print("Movimentações".center(40, '-'))
        for movimentacao in movimentacoes:
            print(f'''
{movimentacao['Situação'].center(40,'-')}
Tipo: {movimentacao['Tipo']} Data Hora: {movimentacao['Data/Hora']}
Nome: {movimentacao['Nome']} Quantidade: {movimentacao['Valor']}
            ''')
        print('-'*40)