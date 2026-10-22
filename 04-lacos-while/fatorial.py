# Faça um programa que leia um número e retorne o fatorial
# 4! = 4 x 3 x 2 x 1

try:
    numero = int(input("Digite um número: "))
    fat = 1

    if numero < 0:
        print("Não existe fatorial de número negativo.")
    else:
        while numero > 1:
            fat = fat * numero
            numero -= 1

        print(f"O fatorial é: {fat}")

except ValueError:
    print("Entrada inválida! Digite números inteiros.")

