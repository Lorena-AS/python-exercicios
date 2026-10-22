
#Crie um programa para jogar JOKENPO, usando a função random.randint
import random
import time
print('Jokenpo! Jogue [1]Pedra, [2]Papel ou [3]Tesoura')

while True:
    try:
        jogador1 = int(input('Sua vez! Escolha um ítem (ou 0 para parar): '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if jogador1 == 0:
        print('Jogo encerrado!')
        break

    jogador2 = random.randint(1,3)

    time.sleep(1)
    print('Jo')
    time.sleep(1.3)
    print('Ken')
    time.sleep(1.1)
    print('Po!')

    print(f'Seu adversário jogou: {jogador2}')
    time.sleep(1)

    if jogador1 == jogador2:
        print('Empate!')
    elif jogador1 == 1 and jogador2 == 3:
        print('Você ganhou!')
    elif jogador1 == 2 and jogador2 == 1:
        print('Você ganhou!')
    elif jogador1 == 3 and jogador2 == 2:
        print('Você ganhou!')
    else:
        print('Você perdeu!')