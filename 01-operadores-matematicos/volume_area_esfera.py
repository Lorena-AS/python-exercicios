# Escreva um programa que leia o raio de uma esfera e calcule seu volume e área.
# V = (4/3) * π * r³
# A = 4 * π * r²

raio = float(input('Digite o raio da esfera: '))

volume = (4 / 3) * 3.14159265359 * raio ** 3
area = 4 * 3.14159265359 * raio ** 2

print(f'Uma esfera com raio {raio} tem:\n'
    f'Um volume de {volume:.2f}\n'
    f'E uma área de {area:.2f}.')