# Elaborar um programa em que o usuário deve preencher uma matriz 5x2.
# Exibir todos os valores digitados e o maior valor de cada linha.

matriz = []

for i in range(5):
    linha = []

    for j in range(2):
        while True:
            try:
                numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
                linha.append(numero)
                break

            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    matriz.append(linha)

print("\nValores digitados:")
for linha in matriz:
    print(linha)

print("\nMaior valor de cada linha:")
for i in range(5):
    print(f"Linha {i + 1}: {max(matriz[i])}")