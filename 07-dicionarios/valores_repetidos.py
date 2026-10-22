#Elaborar um programa para verificar se existem valores repetidos no dicionário
# (ou seja, se não há duas chaves com o mesmo valor). Exibir mensagem caso exista algum valor repetido ou não.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

valores = list(dados.values())

if len(valores) != len(set(valores)):
    print('Existem valores repetidos.')
else:
    print('Não existem valores repetidos.')