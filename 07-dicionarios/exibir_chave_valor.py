# Elaborar um programa para exibir todos os pares chave-valor no seguinte formato “chave=valor”.

dados = {'nome': 'Sandro', 'idade': 30, 'cidade': 'São Paulo', 'estado': 'São Paulo'}

for chave, valor in dados.items():
    print(f'{chave}={valor}')