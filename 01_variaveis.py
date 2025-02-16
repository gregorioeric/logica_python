"""
O que é variavel?
Variavel é um container que armazenada dados
Quais os tipos de dados?
string, inteiros, float, booleana
"""

# string - é sempre representado por aspas duplas ou simples.
nome = "Eric Gregorio de Aquino"
comida = 'Pizza'
email = "dubstep@dubstep.com"

# A função print() é usada para mostrar os dados de uma variavel
# o print() é responsavel pela saida de dados
print(email)

# a palavra reservada f que está dentro dos parenteses e 
# antes das apas significa f-string serve para formatar 
# o conteudo da string, nos permitindo incluir a variavel 
# em qualquer parte da string utilizando as {}
print(f"Seu nome é: {nome} e sua comida favorita é: {comida}")
print('Seu nome é: ')
print(nome)

# Inteiro - são somente numeros, sem casas decimais
# e não pode estar entre aspas
idade = 45
quantidade = 250
ano = 2025

print(f'Sua idade é: {idade}')

# float - são numeros que tem casas decimais
# e tambem não pode estar entre aspas 
price = 450.89
metros = 6.50

print(f'Este tenis custa: R$ {price}')

'''
booleana - recebe um unico valor, ou verdadeiro ou falso
representado pelas palavras reservadas True e False
OBSERVAÇÃO: Essas duas palavras são case sensitive, o que é isso
reparem que as palavras True e False estão com a primeira
letra maiuscula, não se esqueçam disso, toda vez que você usar
uma variavel do tipo booleana as palavras Ture e False a primeira
letra tem que ser maiuscula.
'''
estudade_tem_premissao = False

if estudade_tem_premissao:
    print('Estudante tem permissão para entrar na escola!')
else:
    print('Estudante não tem permissao para entrar na escola!')
