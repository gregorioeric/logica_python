# as palavras nome, nota_01, nota_02 e nota_03 são variaveis
nome = 'Eric Gregorio' # string
nota_01 = 8 # number
nota_02 = 5
nota_03 = 5

porcentage_30 = 30 
porcentage_40 = 40

resultado_a = nota_01 * porcentage_30 / 100
resultado_b = nota_02 * porcentage_30 / 100
resultado_c = nota_03 * porcentage_40 / 100

resultado_total = resultado_a + resultado_b + resultado_c

print(f'Nota final do primeiro bimestre do aluno {nome} e:')
print(resultado_total)

while True:
    nome_completo = input("Digite seu Nome Completo: ")
    print(type(nome_completo))
    if nome_completo.replace(" ", "").isalpha():
        break
    else:
        print("Por favor, digite somente letras.")

print(f"O cadastro do usuario {nome_completo}, foi criado com sucesso")