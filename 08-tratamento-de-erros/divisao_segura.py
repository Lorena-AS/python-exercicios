# Uso simples de Try Except:

try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um outro número: '))
    print(f'{n1} / {n2} = {n1 / n2}')

except ZeroDivisionError:
    print('Não se divide por 0.')

except ValueError:
    print('Apenas números inteiros são aceitos.')