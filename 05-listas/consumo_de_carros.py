# Elaborar um programa que o usuário deve preencher uma lista com os modelos de cinco carros.
# O usuário também deve preencher outra lista com o consumo desses carros, isto é,
# quantos quilômetros cada um deles faz com um litro de combustível.

# Calcule e mostre:
# (a) O modelo de carro mais econômico;
# (b) Quantos litros de combustível cada um dos carros cadastrados consome
# para percorrer uma distância de 1.000 quilômetros.

modelos = []
consumos = []

for i in range(5):
    modelo = input(f'Digite o modelo do {i + 1}º carro: ')
    modelos.append(modelo)

    while True:
        try:
            consumo = float(input(f'Quantos km/l o {modelo} faz? '))
            if consumo > 0:
                consumos.append(consumo)
                break
            print('O consumo deve ser maior que zero.')
        except ValueError:
            print('Entrada inválida! Digite um número.')

indice = consumos.index(max(consumos))

print(f'\nCarro mais econômico: {modelos[indice]}')

print('\nConsumo para percorrer 1.000 km:')
for i in range(5):
    litros = 1000 / consumos[i]
    print(f'{modelos[i]}: {litros:.2f} litros')