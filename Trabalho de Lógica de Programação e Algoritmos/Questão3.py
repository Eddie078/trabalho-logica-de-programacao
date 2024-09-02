#Questão 3
#Função para verificar o serviço desejado
def escolha_servico(pergunta):
    print('''
    Entre com o tipo de serviço desejado:\n
    DIG - Digitalização
    ICO - Impressão Colorida
    IPB - Impressão Preto e Branco
    FOT - Fotocópia
    ''')
    print()

    #laço para forçar a escolha de uma opção válida
    while True:
        servico = input(pergunta).upper()

        #Opções a serem escolhidas
        if servico == 'DIG' or servico == 'ICO' or servico == 'IPB' or servico == 'FOT':
            if servico == 'DIG':
                return valorDig
            elif servico == 'ICO':
                return valorIco
            elif servico == 'IPB':
                return valorIpb
            else:
                return valorFot
            break
        #Na falta de uma opção válida, solicita o tipo de serviço novamente
        else:
            print('Escolha inválida. Entre com o tipo de serviço novamente.')
            print('''
            Entre com o tipo de serviço desejado:\n
            DIG - Digitalização
            ICO - Impressão Colorida
            IPB - Impressão Preto e Branco
            FOT - Fotocópia
            ''')
            print()
            continue

#Função para receber e retornar a quantidade de páginas
def num_pagina(pergunta):
    #laço para forçar a escolha de uma opção válida
    while True:
        #Tratativa de possíveis erros utilizando TRY / EXCEPT
        try:
            #Variáveis globais criadas para uso no programa principal
            global pags, pctdesc, valordesc

            #Solicitação do número de páginas
            pags = int(input(pergunta))

            #Verifica se o valor informado atende aos critérios estipulados
            #Se o valor for menor ou igual a 0 ou maior ou igual a 20000, refaz a pergunta
            if pags <= 0 or pags >= 20000:
                print('Não aceitamos pedidos com menos de 1 página ou mais que 20.000.')
                print('Por favor, entre com o número de páginas novamente.\n')
                continue

            #Menos de 20 páginas. Sem desconto.
            if pags < 20:
                pctdesc = 0
                valordesc = 0
                return pags * escolhido

            #Menos de 200 páginas. 15% de desconto.
            #Calcula o valor do desconto e também o valor total do serviço já com o desconto aplicado
            elif pags < 200:
                valor = pags * escolhido
                pctdesc = 15
                valordesc = (valor * pctdesc) / 100
                desconto = valor - valordesc
                return desconto

            #Menos de 2000 páginas. 20% de desconto.
            elif pags < 2000:
                valor = pags * escolhido
                pctdesc = 20
                valordesc = (valor * pctdesc) /100
                desconto = valor - valordesc
                return desconto

            #Menos de 20000 páginas. 25% de desconto.
            elif pags < 20000:
                valor = pags * escolhido
                pctdesc = 25
                valordesc = (valor * pctdesc) / 100
                desconto = valor - valordesc
                return desconto
            #sai do laço
            break
        #Se a opção for inválida, retorna à pergunta
        except:
            print('Valor inválido. Insira novamente.')

#Função para verificação de serviço adicional
def servico_extra(pergunta):
    # laço para forçar a escolha de uma opção válida
    while True:
        # Tratativa de possíveis erros utilizando TRY / EXCEPT
        try:
            #Solicita ao usuário qual opção de serviço adicional deseja e verifica se o valor informado se enquadra nos critérios estipulados
            servAdicional = int(input(pergunta))

            #Encadernação Simples - R$ 15,00
            if servAdicional == 1:
                valor = 15
                return valor

            #Encadernação com Capa Dura - R$ 40,00
            elif servAdicional == 2:
                valor = 40
                return valor

            #Finaliza a opção de serviço adicional
            elif servAdicional == 0:
                return 0
                break

            #Se a escolha não for uma das opções estipuladas
            else:
                print('Valor inválido. Tente novamente.')
        #Mensagem de erro para validação inválida
        except:
            print('Escolha uma das opções.')

#Variáveis para armazenar os valores dos serviços oferecidos
valorDig = 1.10
valorIco = 1
valorIpb = 0.40
valorFot = 0.20

#Programa principal
#Mensagem de boas vindas com meu nome
nome = 'Eduardo Mikhael Stein Vieira'
print(f'Bem-vindo à Grafica do {nome}!')

#serviço escolhido pelo usuário recebe o serviço desejado
escolhido = escolha_servico('Qual o serviço desejado? ')

#Total de páginas recebe a quantidade de páginas informada pelo usuário
totalPaginas = num_pagina('Quantas paginas necessita? ')

#Adicional recebe, se o cliente desejar, o serviço extra
adicional = servico_extra('''Deseja adicionar algum serviço?\n
    1 - Encadernação Simples - R$ 15,00
    2 - Encadernação com Capa Dura - R$ 40,00
    0 - Não desejo mais nada.
    >> ''')
#Exibe o valor total ao final do programa. Exibe também, o valor do serviço escolhido, a quantidade de paginas solicitadas e o valor da opção de serviço adicional, se solicitada.
#também exibe qual a porcentagem de desconto recebida e o valor desse desconto.
print(f'''Total do serviço: R$ {totalPaginas + adicional:.2f} 
(Serviço: R$ {escolhido:.2f} * páginas: {int(pags)} + extra: R$ {adicional:.2f}.) 
Desconto de {pctdesc}% (R$ {valordesc:.2f})''')