# Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
# Ao final deve mostrar a quantidade de vitórias

import random

vitorias = 0

while True:
    pc = random.randint(1, 10)

    escolha = int(input("Escolha Par[1] ou Impar[2]: "))

    while escolha != 1 and escolha != 2:
        escolha = int(input("Erro. Escolha Par[1] ou Impar[2]: "))

    if escolha == 2:
        print("Escolha: Impar")
    else:
        print("Escolha: Par")

    numero = int(input("Digite um número: "))

    print(f"O pc escolheu: {pc}. \n"
          f"{numero} + {pc} = {numero + pc}")

    if (numero + pc) % 2 == 0 and escolha == 1:
        print("Você ganhou!")
        vitorias += 1
    elif (numero + pc) % 2 == 1 and escolha == 2:
        print("Você ganhou!")
        vitorias += 1
    else:
        print("Você perdeu.")
        break

print(f"Quantidade de vitórias: {vitorias}")