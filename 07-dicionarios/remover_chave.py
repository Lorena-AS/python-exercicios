# Elaborar um programa que permite o usuário informar uma chave a ser removida.
# Remova do dicionário o par referente a essa chave, caso ela exista.
# Se a chave informada não estiver no dicionário, exiba uma mensagem de aviso.
# Mostre o dicionário atualizado após a operação.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

chave = input('Digite a chave que deseja remover: ')

if chave in dados:
    del dados[chave]
else:
    print('A chave informada não existe no dicionário.')

print(dados)