# Elaborar um programa que tenha que ler do usuário 5 pares de informações (nome e idade).
# Crie um dicionário desses dados fornecidos e, ao final, imprima o dicionário.

pessoas = {}

for i in range(5):
    nome = input(f'Digite o nome da pessoa {i + 1}: ')

    while True:
        try:
            idade = int(input(f'Digite a idade de {nome}: '))
            break
        except ValueError:
            print('Entrada inválida! Digite uma idade inteira.')

    pessoas[nome] = idade

print(pessoas)