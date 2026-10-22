# Crie uma função que receba um dicionário e retorne a quantidade de pares chave-valor presentes nele.

def quantidade_pares(dicionario):
    return len(dicionario)

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

print('Quantidade de pares:', quantidade_pares(dados))