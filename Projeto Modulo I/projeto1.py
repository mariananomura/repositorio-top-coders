import json
import os.path
import sys
from unicodedata import category

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

dados = obter_dados()

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for dicionario in dados:
        if dicionario['categoria'] not in lista_categorias:
            lista_categorias.append(dicionario['categoria'])
    return(lista_categorias)


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    itens_categoria = []
    for dicionario in dados:
        if dicionario['categoria'] == categoria:
            itens_categoria.append(dicionario)
    return(itens_categoria)

#categoria = 'agro_industria_e_comercio'
#lista_categorias = listar_por_categoria(dados, categoria)
#print(lista_categorias)

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    
    item_mais_caro = dados[0]
    for item_dicionario in dados:
        if float(item_dicionario['preco']) > float(item_mais_caro['preco']):
            item_mais_caro = item_dicionario
    return(item_mais_caro)

#categoria = 'agro_industria_e_comercio'
#item_mais_caro = produto_mais_caro(dados, categoria)
#print(f'O item mais caro é {item_mais_caro}.')


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    item_mais_barato = dados[0]
    for item_dicionario in dados:
        if float(item_dicionario['preco']) < float(item_mais_barato['preco']):
            item_mais_barato = item_dicionario
    return(item_mais_barato)

#categoria = 'agro_industria_e_comercio'
#item_mais_barato = produto_mais_barato(dados, categoria)
#print(f'O item mais barato é {item_mais_barato}.')

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_10_mais_caros = sorted(dados, key=lambda valor: float(valor['preco']), reverse=True) 
    return lista_10_mais_caros[:10]

#lista = top_10_caros(dados)
#for item in lista:
#    print(item)
    

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    lista_10_mais_baratos = sorted(dados, key=lambda valor: float(valor['preco'])) 
    return lista_10_mais_baratos[:10]


def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    print('Seja bem-vindo(a) ao portal de produtos!\nEscolha uma das opções para continuar:')
    
    escolha_usuario = -1

    while escolha_usuario !=0:

        print(
        '1. Listar categorias\n'
        '2. Listar produtos de uma categoria\n'
        '3. Produto mais caro por categoria\n'
        '4. Produto mais barato por categoria\n'
        '5. Top 10 produtos mais caros\n'
        '6. Top 10 produtos mais baratos\n'
        '0. Sair')

        escolha_usuario=int(input('Digite o número da opção desejada: '))

        if escolha_usuario==1:
            lista_categorias= listar_categorias(dados)
            for categoria in lista_categorias:
                print(categoria.upper())

        elif escolha_usuario==2:
            lista_categorias= listar_categorias(dados)
            categoria = input('Digite a categoria desejada: ')
            if categoria not in lista_categorias:
                print('Opção inválida!')
                categoria = input('Digite a categoria desejada: ')
            else:
                lista_produtos = listar_por_categoria(dados, categoria)
                print(f'Produtos disponíveis na categoria {categoria}:\n')
                for produto in lista_produtos:
                    print(f'- {produto}\n')

        elif escolha_usuario==3:
            print('ok')
        elif escolha_usuario==4:
            print('ok')
        elif escolha_usuario==5:
            print('ok')
        elif escolha_usuario==6:
            print('ok')
        elif escolha_usuario==0:
            print('Serviço encerrado!\nAté mais!')
            break
        else:
            print('Opção inválida!')
# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
