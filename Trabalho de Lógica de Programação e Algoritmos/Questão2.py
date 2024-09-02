#Questão 2
#Mensagem de boas vindas com o nome
nome = 'Eduardo Mikhael Stein Vieira'
print(f'Bem-vindo à Açaiteria do {nome}')

#Apresentação do Menu ao usuário
print('-' * 21, 'CARDÁPIO', '-' * 21)
print('-' * 52)
print('-' * 6, '|', 'TAMANHO', '|', 'CUPUAÇU (CP)', '|', 'AÇAÍ (AC)', '|', '-' * 6)
print('-' * 6, '|', ' ' * 2, 'P', ' ' *2, '|', ' ', 'R$  9,00', ' ' * 1, '|', 'R$ 11,00', ' |', '-' * 6)
print('-' * 6, '|', ' ' * 2, 'M', ' ' *2, '|', ' ', 'R$ 14,00', ' ' * 1, '|', 'R$ 16,00', ' |', '-' * 6)
print('-' * 6, '|', ' ' * 2, 'G', ' ' *2, '|', ' ', 'R$ 18,00', ' ' * 1, '|', 'R$ 20,00', ' |', '-' * 6)
print('-' * 52)

#Variável para o controle do total do pedido
total = 0

#Variáveis para armazenar o valor dos tamanhos da opção CUPUAÇU
preco_cp_p = 9
preco_cp_m = 14
preco_cp_g = 18
#Variáveis para armazenar o valor dos tamanhos da opção AÇAÍ
preco_ac_p = 11
preco_ac_m = 16
preco_ac_g = 20

while True:
    #Solicitação da opção de sabor ao cliente (CP ou AC)
    sabor = input('Informe o sabor desejado (CP / AC): ').upper()

    #Se a opção for CP, inicia a solicitação do tamanho
    if sabor == 'CP':
        #Solicitação da opção do tamanho
        tamanho = input('Informe o tamanho desejado (P / M / G): ').upper()

        while True:
            #Validação do tamanho escolhido e mensagem referente à escolha feita
            if tamanho in ('P', 'M', 'G'):
                #Opção P
                if tamanho == 'P':
                    print(f'Você escolheu um CUPUAÇU no tamanho {tamanho} no valor de: R$ {preco_cp_p:.2f}')
                    #Variável para armazenar o valor do produto
                    total += preco_cp_p
                    print()
                #Opção M
                elif tamanho == 'M':
                    print(f'Você escolheu um CUPUAÇU no tamanho {tamanho} no valor de: R$ {preco_cp_m:.2f}')
                    # Variável para armazenar o valor do produto
                    total += preco_cp_m
                    print()
                #Opção G
                elif tamanho == 'G':
                    print(f'Você escolheu um CUPUAÇU no tamanho {tamanho} no valor de: R$ {preco_cp_g:.2f}')
                    # Variável para armazenar o valor do produto
                    total += preco_cp_g
                    print()
                #saída do laço para seguir com adicional
                break

                #Se a escolha do tamanho for inválida, apresenta uma mensagem e volta ao laço
            else:
                print('Tamanho inválido. Tente novamente.')
                tamanho = input('Informe o tamanho desejado (P / M / G): ').upper()

        #Pergunta ao cliente se deseja mais alguma coisa
        adicional = input('Deseja mais alguma coisa? (S / N): ').upper()

        #Se o cliente escolher S, retorna ao inicio do laço para escolher um novo produto
        if adicional == 'S':
            continue
        #Se o cliente escolher N, finaliza o laço e termina a venda
        elif adicional == 'N':
            break
        # Se o cliente escolher uma opção inválida, retorna à opção de adicional
        else:
            print('Opção inválida. Tente novamente')
            adicional = input('Deseja mais alguma coisa? (S / N): ').upper()
            if adicional == 'N':
                break

    elif sabor == 'AC':
        # Solicitação da opção do tamanho
        tamanho = input('Informe o tamanho desejado (P / M / G): ').upper()

        while True:
            # Validação do tamanho escolhido e mensagem referente à escolha feita
            if tamanho in ('P', 'M', 'G'):
                # Opção P
                if tamanho == 'P':
                    print(f'Você escolheu um AÇAÍ no tamanho {tamanho} no valor de: R$ {preco_ac_p:.2f}')
                    # Variável para armazenar o valor do produto
                    total += preco_ac_p
                    print()
                # Opção M
                elif tamanho == 'M':
                    print(f'Você escolheu um AÇAÍ no tamanho {tamanho} no valor de: R$ {preco_ac_m:.2f}')
                    # Variável para armazenar o valor do produto
                    total += preco_ac_m
                    print()
                # Opção G
                elif tamanho == 'G':
                    print(f'Você escolheu um AÇAÍ no tamanho {tamanho} no valor de: R$ {preco_ac_g:.2f}')
                    # Variável para armazenar o valor do produto
                    total += preco_ac_g
                    print()
                # saída do laço para seguir com adicional
                break
                # Se a escolha do tamanho for inválida, apresenta uma mensagem e volta ao laço
            else:
                print('Tamanho inválido. Tente novamente.')
                tamanho = input('Informe o tamanho desejado (P / M / G): ').upper()
        #Pergunta ao cliente se deseja mais alguma coisa
        adicional = input('Deseja mais alguma coisa? (S / N): ').upper()

        #Se o cliente escolher S, retorna ao inicio do laço para escolher um novo produto
        if adicional == 'S':
            continue
        #Se o cliente escolher N, finaliza o laço e termina a venda
        elif adicional == 'N':
            break
        #Se o cliente escolher uma opção inválida, retorna à opção de adicional
        else:
            print('Opção inválida. Tente novamente')
            adicional = input('Deseja mais alguma coisa? (S / N): ').upper()
            if adicional == 'N':
                break
    #Se a opção de sabor for inválida, retorna ao início do laço
    else:
        print('Sabor inválido. Tente Novamente')
        continue

#Mensagem com o valor total a ser pago
print(f'O valor total a ser pago é: {total:.2f}')
print('Encerrando o programa...')