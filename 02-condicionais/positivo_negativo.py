# Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

try:
    numero = float(input('Digite um número: '))

    if numero > 0:
        print('Seu número é positivo!')
    elif numero < 0:
        print('Seu número é negativo! :(')
    else:
        print('Seu número é zero!')

except ValueError:
    print('Entrada inválida! Digite um número.')
