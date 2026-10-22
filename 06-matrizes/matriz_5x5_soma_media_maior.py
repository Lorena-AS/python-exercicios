# Elaborar um programa que contenha uma matriz 5x5.
# O usuário deve preencher a matriz com números inteiros.
# Ao final, exibir a soma, a média e o maior valor digitado.

matriz = []
soma = 0
maior = None

for i in range(5):
    linha = []

    for j in range(5):
        while True:
            try:
                numero = int(input(f"Digite um número para a posição [{i}][{j}]: "))
                linha.append(numero)
                soma += numero

                if maior is None or numero > maior:
                    maior = numero

                break

            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    matriz.append(linha)

media = soma / 25

print("\nMatriz digitada:")
for linha in matriz:
    print(linha)

print(f"\nSoma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
print(f"Maior valor digitado: {maior}")