#Questão 1
#Exigência A - Saudação com o meu nome
nome = 'Eduardo Mikhael Stein Vieira'
print(f'Bem-vindo à Loja do {nome}')

#Exigência B - Solicitação do valor do produto e quantidade
preco = int(input('Informe o valor do produto: '))
qtd = int(input('Informe a quantidade do produto: '))

#Armazenamento do valor total
total = preco * qtd

#Armazenamento dos valores de descontos a serem aplicados
desconto4 = ((total * 4) / 100)  #Desconto de 4%
desconto7 = ((total * 7) / 100)  #Desconto de 7%
desconto11 = ((total * 11) / 100)  #Desconto de 11%

#Exigências C, D e E - Validações de Menor, Igual e Maior / if, elif e else / Valor total com e sem desconto
if total < 2500:
    #Desconto de 0%
    print(f'Valor SEM desconto: {total:.2f}')

elif total < 6000:
    #Desconto de 4%
    print(f'Valor SEM desconto: {total:.2f}')
    print(f'Valor COM desconto: {total - desconto4:.2f}')

elif total < 1000:
    #Desconto de 7%
    print(f'Valor SEM desconto: {total:.2f}')
    print(f'Valor COM desconto: {total - desconto7:.2f}')

else:
    #Desconto de 11%
    print(f'Valor SEM desconto: {total:.2f}')
    print(f'Valor COM desconto: {total - desconto11:.2f}')
