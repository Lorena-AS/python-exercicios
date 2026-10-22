# Converta graus celsius para fahrenheit:

cel1 = 0

while cel1 > -5:
    try:
        cel1 = float(input("Informe a temperatura em celsius a ser convertida: "))
    except ValueError:
        print("Entrada inválida! Digite números inteiros.")
    if cel1 > -5:
        conversao = (cel1 * 1.8) + 32
        print(f"Programa encerrado. {cel1}ºC = {conversao:.2f}ºF.")
    else:
        conversao = (cel1 * 1.8) + 32
        print(f"Programa encerrado. {cel1}ºC = {conversao:.2f}ºF.")