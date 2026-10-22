
#Calculadora

try:
    n1 = float(input("Insira o 1º número: "))
    conta = input("Insira o operador: ")
    n2 = float(input("Insira o 2ª número: "))

    if conta == "+":
        final = n1 + n2
        print(f'Seu resultado é: {final}')
    elif conta == "-":
        final = n1 - n2
        print(f'Seu resultado é: {final}')
    elif conta == "*":
        final = n1 * n2
        print(f'Seu resultado é: {final}')
    elif conta == "/":
        if n2 == 0:
            print('Não é possível dividir por zero!')
        else:
            final = n1 / n2
            print(f'Seu resultado é: {final}')
    else:
        print('Operador inválido!')

except ValueError:
    print('Entrada inválida! Digite números válidos.')
