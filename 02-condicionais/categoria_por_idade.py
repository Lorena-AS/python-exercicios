# Crie um programa que verifica a idade de jogadores (para um time de futebol) e retorna a categoria dela.

try:
    idade = int(input("Informe sua idade: "))

    if 5 <= idade <= 10:
        print("Categoria: Infantil")
    elif 11 <= idade <= 15:
        print("Categoria: Juvenil")
    elif 16 <= idade <= 20:
        print("Categoria: Junior")
    elif 21 <= idade <= 25:
        print("Categoria: Profissional")
    else:
        print("Fora de categoria.")

except ValueError:
    print("Entrada inválida! Digite uma idade em números inteiros.")