# 4) Elaborar um programa que leia uma lista que contenha 20 números inteiros
# e em seguida o programa deve exibir o maior e o menor número.

lista = []

for i in range(20):
    while True:
        try:
            numero = int(input(f'Digite o {i + 1}º número inteiro: '))
            lista.append(numero)
            break
        except ValueError:
            print('Entrada inválida! Digite um número inteiro.')

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')