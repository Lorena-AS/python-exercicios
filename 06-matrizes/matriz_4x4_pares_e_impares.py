# Elaborar um programa que contenha uma matriz 4x4.
# Substituir os números pares por 1 e os ímpares por 0.
# Ao final, exibir a nova matriz.

matriz = []

for i in range(4):
    linha = []

    for j in range(4):
        while True:
            try:
                numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
                linha.append(numero)
                break

            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    matriz.append(linha)

for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

print("\nNova matriz:")
for linha in matriz:
    print(linha)