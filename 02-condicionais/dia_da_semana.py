# Crie um programa que, ao digitar um número de 1 a 7, retorna o dia da semana referente a ele. Utilize Case.

def dia_semana(numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"

while True:
    try:
        n_inteiro = int(input("Digite um número inteiro de 1 a 7: "))

        if n_inteiro in range(1, 8):
            print(dia_semana(n_inteiro))
            break
        else:
            print("Número inválido! Digite um número de 1 a 7.")

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")