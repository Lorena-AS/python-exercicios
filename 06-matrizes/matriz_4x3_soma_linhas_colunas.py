# Elaborar um programa em que o usuário deve preencher uma matriz 4x3 com números inteiros.
# Ao final, exibir a soma de cada linha e a soma de cada coluna.

matriz = []

for i in range(4):
    linha = []

    for j in range(3):
        while True:
            try:
                numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
                linha.append(numero)
                break
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    matriz.append(linha)

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print("\nSoma de cada linha:")
for i in range(4):
    print(f"Linha {i + 1}: {sum(matriz[i])}")

print("\nSoma de cada coluna:")
for j in range(3):
    soma_coluna = sum(matriz[i][j] for i in range(4))
    print(f"Coluna {j + 1}: {soma_coluna}")