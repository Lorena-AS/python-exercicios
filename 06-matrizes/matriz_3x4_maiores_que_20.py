# Elaborar um programa que contenha uma matriz 3x4.
# Exibir os valores maiores que 20, a quantidade e suas posições na matriz.

matriz = []
maiores = []

for i in range(3):
    linha = []

    for j in range(4):
        while True:
            try:
                numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
                linha.append(numero)

                if numero > 20:
                    maiores.append((numero, i, j))

                break

            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print("\nValores maiores que 20:")
for numero, i, j in maiores:
    print(f"Valor: {numero}, posição: [{i}][{j}]")

print(f"\nQuantidade de valores maiores que 20: {len(maiores)}")