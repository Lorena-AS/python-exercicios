#Elaborar um programa que leia uma nova chave e um valor do usuário e os adicione ao dicionário.
# Caso a chave já exista, atualize o valor existente para o novo valor fornecido
# No final, exiba o dicionário resultante.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

chave = input('Digite uma nova chave: ')
valor = input('Digite um valor: ')

dados[chave] = valor

print(dados)