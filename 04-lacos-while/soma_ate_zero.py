# Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
# No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).

acumulador = 0
qtd = 0

while True:
    try:
        n = int(input("Digite um número para somar (0000 para encerrar): "))

        if n == 0:
            break

        acumulador += n
        qtd += 1

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

print(f'Quantidade digitada: {qtd}, soma total: {acumulador}')