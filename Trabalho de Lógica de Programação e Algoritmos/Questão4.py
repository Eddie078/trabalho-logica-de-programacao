#Função para cadastro de livros
def cadastrar_livro(identificador):
    # Exibe o menu de cadastro de livros
    print('-' * 48)
    print('-' * 13, 'MENU CADASTRAR LIVRO', '-' * 13)

    #Identificador global para incrementação a cada novo cadastro
    global id_global

    #Solicitação dos dados do livro a ser cadastrado
    identificador = int(id_global) + 1
    print(f'ID do livro: {identificador}')
    nome = input('Nome do livro: ').upper()
    autor = input('Nome do autor: ').upper()
    editora = input('Nome da editora: ').upper()
    id_global += 1

    # Cria um dicionário com os dados do livro
    livro = {'ID': identificador, 'Nome': nome, 'Autor': autor, 'Editora': editora}
    print()

    #Retorna o dicionário para inclusão na lista
    return livro


#Função para consulta de livros
def consultar_livro():
    while True:
        try:
            # Exibe o menu de consulta de livros
            print('-' * 48)
            print('-' * 13, 'MENU CONSULTAR LIVRO', '-' * 13)

            consulta = int(input('''Escolha a opção desejada:
        1 - Consultar Todos os Livros
        2 - Consultar Livro por ID
        3 - Consultar Livro(s) por autor
        4 - Retornar
        >> '''))

            #Opção para consulta de todos os livros
            if consulta == 1:
                if not lista_livro:  #Verifica se existe algum livro já cadastrado
                    print('Nenhum livro cadastrado.')
                    break
                else:
                    for nome in lista_livro:
                        print('-' * 48)
                        print(f'ID: {nome['ID']}')
                        print(f'Nome: {nome['Nome']}')
                        print(f'Autor: {nome['Autor']}')
                        print(f'Editora: {nome['Editora']}')
                        print()

            #Opção para consulta por Id
            elif consulta == 2:
                if not lista_livro:  #Verifica se existe algum livro já cadastrado
                    print('Nenhum livro cadastrado.')
                    break

                #Solicita um Id ao usuário
                consulta_id = int(input('Digite o ID do livro: '))

                #Verifica a existência do Id informado dentro da lista
                if consulta_id <= 0 or consulta_id > len(lista_livro):
                    print('ID inválido, tente novamente.')

                #Se o id for encontrado, exibe as informações contidas na lista
                for id in lista_livro:
                    if consulta_id == id['ID']:
                        print('-' * 48)
                        print(f'ID: {id['ID']}')
                        print(f'Nome: {id['Nome']}')
                        print(f'Autor: {id['Autor']}')
                        print(f'Editora: {id['Editora']}')
                        print()

            #Opção para consulta por Autor
            elif consulta == 3:
                if not lista_livro:  #Verifica se existe algum livro já cadastrado
                    print('Nenhum livro cadastrado.')
                    break

                #Solicita um autor ao usuário
                consulta_autor = input('Digite o autor do(s) livro(s): ').upper()

                #Inicia a variável como FALSE para realizar o controle
                encontrado = False

                #Verifica na lista se existe o autor buscado
                for autor in lista_livro:

                    #Se o autor for encontrado, exibe as informações contidas na lista
                    if consulta_autor == autor['Autor']:
                        print('-' * 48)
                        print(f'ID: {autor['ID']}')
                        print(f'Nome: {autor['Nome']}')
                        print(f'Autor: {autor['Autor']}')
                        print(f'Editora: {autor['Editora']}')
                        print()

                        #Ao ser encontrado um autor, altera a variavel de controle para TRUE
                        encontrado = True

                #Se o autor não for encontrado, exibe uma mensagem
                if not encontrado:
                    print('Não foram encontrados livros desse autor.')

            #Opção para retornar ao Menu Principal
            elif consulta == 4:
                break
            #Mensagem exibida caso o usuário escolha uma opção inválida
            else:
                print('Opção inválida. Tente novamente.')

        #Tratamento de exceção, para o caso do usuário entrar com um valor inválido
        except ValueError:
            print('Valor inválido. Tente novamente.')


#Função para remoção de livros
def remover_livro():
    print('-' * 48)
    print('-' * 14, 'MENU REMOVER LIVRO', '-' * 14)

    while True:
        try:
            if not lista_livro:  #Verifica se existe algum livro já cadastrado
                print('Nenhum livro cadastrado.')
                break
            #Solicita o Id do livro a ser removido
            remove = int(input('Digite o ID do livro a ser removido: '))
            # Inicia a variável como FALSE para realizar o controle
            id_encontrado = False
            # Verifica a existência do Id informado dentro da lista
            if remove <= 0 or remove > len(lista_livro):
                print('Id inválido. Tente novamente com um Id válido')
                print()
                continue
            # Se o Id for encontrado, exibe uma mensagem de confirmação
            for id in lista_livro:
                if remove == id['ID']:
                    id_encontrado = True
                    escolha = input('Tem certeza que deseja remover esse livro? [S/N] ').upper()

                    #Se for confirmado, remove o livro
                    if escolha == 'S':
                        lista_livro.remove(id)
                        print(f'Livro {id['Nome']} removido com sucesso!')
                        print()
            #Se nenhum Id for encontrado, exibe uma mensagem
            if not id_encontrado:
                print('Nenhum livro cadastrado com esse Id.')
                print()
            #Finaliza o laço
            break
        # Tratamento de exceção, para o caso do usuário entrar com um valor inválido
        except ValueError:
            print('Opção inválida. Tente novamente.')
            print()


#Programa principal

#Boas Vindas com meu nome
meu_nome = 'Eduardo Mikhael Stein Vieira'
print(f'Bem vindo à Livraria do {meu_nome}')

#Implementação da lista vazia
lista_livro = []
#Variável global
id_global = 0

# Exibe o Menu Principal
while True:
    print('-' * 48)
    print('-' * 16, 'MENU PRINCIPAL', '-' * 16)

    try:
        menu = int(input('''Escolha a opção desejada:
        1 - Cadastrar livro
        2 - Consultar livro(s) 
        3 - Remover livro
        4 - Sair
        >> '''))

        #Opção para cadastro de livro
        if menu == 1:
            novo_livro = cadastrar_livro(id_global)
            #Faz uma verificação na lista em busca de livros com o mesmo nome e autor
            for livro in lista_livro:
                #Se outro livro for encontrado, exibe uma mensagem
                if novo_livro['Nome'] == livro['Nome'] and novo_livro['Autor'] == livro['Autor']:
                    print(f'{novo_livro['Nome']} já existe!')
                    #Altera o valor da variável de Id global para -1, assim, o livro repetido nâo obtém esse Id
                    id_global -= 1
                    #Finaliza o laço
                    break
            #Se passar na verificação, realiza o cadastro de um novo livro
            else:
                lista_livro.append(novo_livro)
                print(f'Livro {novo_livro['Nome']} cadastrado com sucesso!')

        #Opção para consulta de livros cadastrados
        elif menu == 2:
            consultar_livro()
        #Opção para remoção de livros cadastrados
        elif menu == 3:
            remover_livro()
        #Opção para encerramento do programa
        elif menu == 4:
            print('Encerrando o programa...')
            break
        #Mensagem exibida caso o usuário escolha uma opção inválida
        else:
            print('Opção inválida. Tente novamente.')
    #Tratamento de exceção, para o caso do usuário entrar com um valor inválido
    except ValueError:
        print('Valor inválido. Tente novamente.')
