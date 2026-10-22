# 2) Elaborar um programa que leia uma lista de 6 números inteiros e mostre
# cada número juntamente com a sua posição na lista.

lista = []

for i in range(6):
    while True:
        try:
            numero = int(input(f'Digite o {i + 1}º número inteiro: '))
            lista.append(numero)
            break
        except ValueError:
            print('Entrada inválida! Digite um número inteiro.')

for posicao, numero in enumerate(lista):
    print(f'Posição {posicao}: {numero}')