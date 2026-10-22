# Elaborar um programa que obtenha todas as chaves do dicionário e as armazene em uma lista,
# e faça o mesmo com todos os valores do dicionário, armazenando-os em outra lista.
# Ao final, exiba as duas listas (lista de chaves e lista de valores).

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

chaves = list(dados.keys())
valores = list(dados.values())

print('Lista de chaves:', chaves)
print('Lista de valores:', valores)