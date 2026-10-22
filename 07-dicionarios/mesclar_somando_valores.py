# Elaborar um programa para mesclar dois dicionários de forma que, quando ambos compartilharem a mesma chave,
# seus valores sejam somados em vez de um sobrescrever o outro.

dicionario1 = {'a': 10, 'b': 20, 'c': 30}
dicionario2 = {'b': 5, 'c': 15, 'd': 40}

mesclado = dicionario1.copy()

for chave, valor in dicionario2.items():
    if chave in mesclado:
        mesclado[chave] += valor
    else:
        mesclado[chave] = valor

print(mesclado)