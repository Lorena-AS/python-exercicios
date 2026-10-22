
print('''Código    |  Nome do Candidato
     11           |  João
     45           |  Maria
     0            |  Voto em Branco
     Outro código |  Voto Nulo''')

try:
    eleitores = int(input("Qual a quantidade de eleitores? "))
    iniciar = 12345
    encerrar = 35719
    joao = 0
    maria = 0
    branco = 0
    nulo = 0
    i = 0

    while i < eleitores:
        codigoi = int(input("Código para iniciar a votação: "))

        if codigoi == iniciar:
            voto = int(input("Qual o seu voto? "))

            if voto == 11:
                joao = joao + 1
            elif voto == 45:
                maria = maria + 1
            elif voto == 0:
                branco = branco + 1
            else:
                nulo = nulo + 1

            i = i + 1
        else:
            print("Código de início incorreto. Tente novamente.")

    codigof = int(input("Digite o código de encerramento: "))

    while codigof != encerrar:
        codigof = int(input("Digite o código correto: "))

    print("Votação encerrada.")

    print(f'''João: {joao}.
    Maria: {maria}.
    Branco: {branco}.
    Nulo: {nulo}.
    Total de votos nulo/branco: {nulo + branco}''')

except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")
