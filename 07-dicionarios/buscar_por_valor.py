# Elaborar um programa que solicite ao usuário para informar um valor e verifique
# se esse valor existe em algum dos pares do dicionário.
# Se existir, exiba todas as chaves que possuem esse valor;
# caso contrário, exiba uma mensagem indicando que o valor não foi encontrado.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

valor = input('Digite um valor para pesquisar: ')

encontrado = False

for chave, valor_dicionario in dados.items():
    if str(valor_dicionario) == valor:
        print(f'Chave encontrada: {chave}')
        encontrado = True

if not encontrado:
    print('Valor não encontrado.')