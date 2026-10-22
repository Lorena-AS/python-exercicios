# Monte uma lista simples.
lista = []

while True:
    try:
        n1 = int(input("Insira um número à lista: "))

        if n1 >= 0:
            lista.append(n1)
        else:
            print('Número negativo. Programa finalizado.')
            break

    except ValueError:
        print('Digite um número!')

print(lista)
