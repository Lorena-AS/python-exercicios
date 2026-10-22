# Elaborar um programa para adicionar um novo par chave-valor ao dicionário,
# modificar um valor existente e acessar uma chave específica.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

dados['profissao'] = 'Programador'
dados['idade'] = 31

chave = input('Digite uma chave para acessar: ')

if chave in dados:
    print(dados[chave])
else:
    print('Chave não encontrada.')

print(dados)