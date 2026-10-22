#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está
# entre a faixa ideal, acima ou abaixo do IMC ideal.

print('Calcule seu IMC!')

try:
    peso = float(input('Informe seu peso: '))
    altura = float(input('Informe sua altura: '))

    if peso <= 0 or altura <= 0:
        print('O peso e a altura devem ser maiores que zero.')
    else:
        imc = peso / (altura ** 2)
        print(f'Seu IMC é {round(imc,2)}')

        if imc < 18.5:
            print('Você está abaixo do peso')
        elif imc <= 25:
            print('Você está com o peso ideal!')
        else:
            print('Você está acima do peso.')

except ValueError:
    print('Entrada inválida! Digite números válidos.')
