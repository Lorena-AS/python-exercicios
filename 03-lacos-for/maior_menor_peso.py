# Escreva um programa que leia o peso de 7 pessoas,
# e no final, mostre qual foi o maior e o menor peso lido

maior = None
menor = None

for i in range(0, 7):
    try:
        peso = float(input("Qual seu peso? "))

        if maior == None and menor == None:
            maior = peso
            menor = peso

        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

    except ValueError:
        print("Entrada inválida! Digite um peso válido.")
        continue

print(f"Maior peso: {maior}. Menor peso: {menor}.")
