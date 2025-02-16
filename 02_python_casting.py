"""
O que typecasting?

É o processo que converte uma variavel em um unico tipo
"""

# int() => é uma função padrão do python que
# constroi um numero inteiro a partir de um literal
# inteiro, um literal float ou um literal string

num_00 = "258741"
num_01 = int(12)
num_02 = int(10.55)
num_03 = int(num_00)

# print(type(num_00))
# print(type(num_03))
# print(num_01)
# print(num_02)
# print(num_03)

# float() => é uma função padrão do python que
# constroi um numero float a partir de um literal
# inteiro, um literal float ou um literal string

float_01 = float(14)
float_02 = float(2.6)
float_03 = float("50")
float_04 = float("491.88")

# print(float_01)
# print(float_02)
# print(float_03)
# print(float_04)

# str() => é uma função padrão do python que
# constrói uma string a partir de uma ampla variedade
# de tipos de dados, incluindo strings,
# literais inteiros e literais flutuantes

string_01 = str(12547869347815)
string_02 = str("Eric 2514 Gregorio 25142")
string_03 = str(123.456)

print(type(string_01))
print(type(string_02))
print(type(string_03))