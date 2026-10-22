# Crie um programa que retorne a tabuada de um número e só pare quando o número digitado for 0000.

contas = ['/', '+', '-', '*']

while True:
    try:
        n = int(input("Digite um número para a tabuada (0000 para encerrar): "))

        if n == 0:
            print("Programa encerrado.")
            break

        conta = input("Informe o tipo de conta (+, -, *, /): ")

        while conta not in contas:
            conta = input("Tipo inválido! Informe (+, -, *, /): ")

        for i in range(1, 11):
            if conta == '+':
                print(f"{n} + {i} = {n + i}")
            elif conta == '-':
                print(f"{n} - {i} = {n - i}")
            elif conta == '*':
                print(f"{n} * {i} = {n * i}")
            elif conta == '/':
                print(f"{n} / {i} = {n / i:.2f}")

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")