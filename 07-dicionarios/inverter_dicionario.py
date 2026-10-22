# Elaborar um programa para inverter o dicionário, trocando suas chaves e valores,
# de forma que cada valor original se torne uma chave e cada chave original se torne correspondente
# Exibir o novo dicionário.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

invertido = {valor: chave for chave, valor in dados.items()}

print(invertido)