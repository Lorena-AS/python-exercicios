# Escreva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final mostre:
# A média de idade do grupo
# Qual é o homem mais velho
# Quantas mulheres têm menos de 20 anos

soma_idade = 0
novas = 0
velho = -1
mais_velho = ''
contador = 0

while contador < 4:
    try:
        sexo = input("Digite seu gênero [F/M]: ").upper().strip()
        if sexo not in ['F', 'M']:
            print("Gênero inválido! Digite F ou M.")
            continue

        nome = input("Digite seu nome: ").strip()
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
            continue

        soma_idade += idade

        if sexo == 'F' and idade < 20:
            novas += 1

        if sexo == 'M' and idade > velho:
            velho = idade
            mais_velho = nome

        contador += 1

    except ValueError:
        print("Idade inválida! Digite um número inteiro.")

print(f'A média de idade de todo o grupo é: {soma_idade / 4:.2f}.')

if mais_velho:
    print(f'O homem mais velho é: {mais_velho}, com {velho} anos.')
else:
    print('Nenhum homem foi informado.')

print(f'Quantidade de mulheres com menos de 20 anos: {novas}')
