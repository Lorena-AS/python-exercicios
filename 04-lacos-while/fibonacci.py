# Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros
# elementos de uma Sequência de Fibonacci

try:
    numero = int(input("Digite um número: "))
    primeiro = 0
    segundo = 1
    contador = 0

    if numero < 0:
        print("Digite um número inteiro positivo.")
    else:
        while contador < numero:
            print(primeiro)
            fib = primeiro + segundo
            primeiro = segundo
            segundo = fib
            contador += 1

except ValueError:
    print("Entrada inválida! Digite um número inteiro.")

