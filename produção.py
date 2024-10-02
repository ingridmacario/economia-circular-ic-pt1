'''ESSE TRABALHO TRATA-SE DE UMA ANÁLISE DE DADOS REALIZADA DURANTE
A MINHA INICIAÇÃO CIENTIFÍCA. CONSISTE EM UMA ANÁLISE BIBLIOGRAFICA ACERCA
DO TEMA "FOMENTO DO BIM PARA IMPLEMENTAÇÃO DA ECONOMIA CIRCULAR NA CONSTRUÇÃO CIVIL"
DE ARTIGOS PUBLICADOS NO ÍNTERIM DE 2010 A 2020. BASE DE DADOS UTILIZADA FOI A
WEB OF SCIENCE.'''


import csv
planilha = []
#abrindo o csv
try:
    with open('Projeto02.csv','r', encoding='utf-8-sig') as arquivo:
        conteudo_planilha = csv.DictReader(arquivo, delimiter=';')
        for linha in conteudo_planilha:
            planilha.append(linha)

except IOError as erro:
    print(f'{erro} ao ler o arquivo.')

'''O DOI é como se fosse o CPF do artigo, logo, é único por artigo. 
Pensando nisso, decidi gerar ele como uma chave de cada um dos dicionários.
Assim, facilitando a manipulação e também a saída do programa.'''
projeto = {linha.pop('DOI'): linha for linha in planilha}
print(f'Dados: {projeto}')

#função media
def media(n1,n2):
    try:
        m = lambda x, y: x / y
        return m(n1,n2)
    except ZeroDivisionError:
        print('Não é possível executar essa operação.')
    except TypeError:
        print('Não é possível executar essa operação, uma vez que contém valores inválidos.')
#função tela
def tela():
    print('-' * 150)

#calculando a fonte que mais aparece.

tela()
print('CALCULANDO A FONTE QUE MAIS APARECE NOS ARTIGOS')
fontes = [linha['Fonte']for linha in planilha]
print(f'{" "*5}Fontes: {fontes}')
fonte = max(fontes, key=fontes.count)
contador_fonte = fontes.count(fonte)
print(f'A fonte {fonte} publicou {contador_fonte} artigos')
tela()

#calculando o idioma que mais aparece

print('IDIOMA QUE APARECE COM MAIOR FREQUENCIA NOS ARTIGOS')
idiomas = [linha['Idioma'] for linha in planilha]
print(idiomas)
idioma = max(idiomas, key=idiomas.count)
contador_idioma = idiomas.count(idioma)
print(f'O idioma que teve maior frequencia nos artigos publicados foi {idioma} com {contador_idioma} artigos.')
tela()

#calculando a palavra-chave que mais aparece

print('PALAVRA-CHAVE QUE APARECE COM MAIOR FREQUENCIA NOS ARTIGOS')
palavra_chaves = [linha['Palavra-chave'] for linha in planilha]
print(f'{" "*5}{palavra_chaves}')
p_chaves = max(palavra_chaves, key=palavra_chaves.count)
contador_p_chaves = palavra_chaves.count(p_chaves)
print(f'{p_chaves} é a palavra chave que mais se repete, com {contador_p_chaves} publicações')
tela()

#calculando o ano em que mais ocorreu publicação

print('ANO DE PUBLICAÇÃO COM MAIOR QUANTIDADE DE ARTIGO PUBLICADO')
anos = [linha["Ano de Publicacao"] for linha in planilha]
print(f'{" "*5} {anos}')
ano_publicacao = max(anos, key=anos.count)
contador_ano_publicacao = anos.count(ano_publicacao)
print(f'Com {contador_ano_publicacao} artigos, {ano_publicacao} foi o ano em que mais ocorreu publicação')
tela()

#calculando a media das citações

print('MÉDIA DAS CITAÇÕES')
soma = 0
contador = 0
citacao = [float(linha['Citacao']) for linha in planilha]
#citacao = {float(linha['Citacao']) for linha in projeto.values()}
for chave,valor in projeto.items():
    print(f'{(" ")*5} O artigo {chave} teve {valor["Citacao"]} citações')
for numero in citacao:
    soma += numero
    contador+=1
print(f'A média das citações dos artigos publicadas no ínterim de 2010 a 2020 é igual a {media(soma, contador):.2f}.')
tela()

#media do numero de paginas

print('MÉDIA DO NÚMERO DE PÁGINAS DOS ARTIGOS')
soma = 0
contador = 0
num_paginas = [float(linha['Numero de Paginas']) for linha in planilha]
print(f'{" "*5} Numero de páginas: {num_paginas}')
for numero in num_paginas:
    soma+=numero
    contador+=1
print(f'A média de paginas dos artigos publicados no interim de 2010 a 2020 foi {media(soma,contador):.2f}.')
tela()










