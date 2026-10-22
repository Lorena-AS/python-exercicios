# Elaborar um programa com uma função que receba o raio de uma esfera.
# O algoritmo deve calcular e exibir a área e o volume da esfera.
# V = (4/3) * π * R³
# A = 4 * π * R²

import math

def esfera(raio):
    volume = (4 / 3) * math.pi * raio ** 3
    area = 4 * math.pi * raio ** 2
    return area, volume

try:
    raio = float(input('Digite o raio da esfera: '))

    if raio < 0:
        print('O raio não pode ser negativo.')
    else:
        area, volume = esfera(raio)
        print(f'Área da esfera: {area:.2f}')
        print(f'Volume da esfera: {volume:.2f}')

except ValueError:
    print('Entrada inválida! Digite um número válido.')