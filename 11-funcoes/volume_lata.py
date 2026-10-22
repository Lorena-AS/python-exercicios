# Elaborar um programa com uma função que receba o raio e a altura de uma
# lata de óleo para calcular e apresentar o valor do volume desta lata,
# dado: V = π*r²*h.

import math

def volume_lata(raio, altura):
    return math.pi * raio ** 2 * altura

try:
    raio = float(input('Digite o raio da lata: '))
    altura = float(input('Digite a altura da lata: '))

    if raio < 0 or altura < 0:
        print('O raio e a altura não podem ser negativos.')
    else:
        volume = volume_lata(raio, altura)
        print(f'O volume da lata é: {volume:.2f}')

except ValueError:
    print('Entrada inválida! Digite números válidos.')