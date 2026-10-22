#Crie um programa que verifica se uma pessoa poderá doar sangue
# considerando a idade e os critérios de saúde.

print('Formulário de doação de sangue')

try:
    peso = float(input('Informe seu peso: '))
    altura = float(input('Informe sua altura: '))

    if peso <= 0 or altura <= 0:
        print('Peso e altura devem ser maiores que zero.')
    else:
        imc = peso / (altura ** 2)

        if imc >= 18.5 and imc <= 25:
            idade = int(input('Informe sua idade: '))

            if idade >= 18 and idade < 60:
                fumante = input('Você fuma?:[S/N] ').strip().upper()

                if fumante == 'N':
                    medicacao = input(
                        'Você usa medicação sob prescrição médica?[S/N]: '
                    ).strip().upper()

                    if medicacao == 'N':
                        jejum = input('Está em jejum?:[S/N] ').strip().upper()

                        if jejum == 'N':
                            print('Você pode prosseguir com a avaliação!')
                        elif jejum == 'S':
                            print('Procure o hemocentro para orientação.')
                        else:
                            print('Resposta inválida. Digite S ou N.')
                    elif medicacao == 'S':
                        print('Informe os medicamentos à equipe.')
                    else:
                        print('Resposta inválida. Digite S ou N.')
                elif fumante == 'S':
                    print('Consulte a equipe sobre sua elegibilidade.')
                else:
                    print('Resposta inválida. Digite S ou N.')
            else:
                print('Verifique os critérios de idade com o hemocentro.')
        else:
            print('Seu IMC está fora da faixa definida.')

except ValueError:
    print('Entrada inválida! Digite números válidos.')

