# Elaborar um programa para renomear uma chave existente do dicionário,
# preservando seu valor associado e mantendo o restante do dicionário inalterado.
# Exibir o novo dicionário.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

chave = input('Digite a chave que deseja renomear: ')

if chave in dados:
    nova_chave = input('Digite o novo nome da chave: ')
    dados[nova_chave] = dados.pop(chave)
    print(dados)
else:
    print('Chave não encontrada.')