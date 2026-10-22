# Elaborar um programa que solicite ao usuário para digitar uma chave e verifique se essa chave existe no dicionário.
# Se a chave existir, exiba o valor correspondente;
# caso contrário, mostre uma mensagem informando que a chave não foi encontrada.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

chave = input('Digite uma chave: ')

if chave in dados:
    print(f'Valor correspondente: {dados[chave]}')
else:
    print('Chave não encontrada.')