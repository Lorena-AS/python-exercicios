# Elaborar um programa com uma função que calcule a aceleração de um corpo
# em movimento conhecendo-se as velocidades inicial e final, e o intervalo de
# tempo medido (a = (v2 − v1)/Δt). Exibir o resultado.

def aceleracao(v1, v2, tempo):
    return (v2 - v1) / tempo

try:
    v1 = float(input('Digite a velocidade inicial: '))
    v2 = float(input('Digite a velocidade final: '))
    tempo = float(input('Digite o intervalo de tempo: '))

    if tempo <= 0:
        print('O intervalo de tempo deve ser maior que zero.')
    else:
        print(f'A aceleração é: {aceleracao(v1, v2, tempo):.2f} m/s²')

except ValueError:
    print('Entrada inválida! Digite números válidos.')