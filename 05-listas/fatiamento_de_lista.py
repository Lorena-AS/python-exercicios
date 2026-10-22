# 1) Dada a lista abaixo:
# Exibir as seguintes listas, derivadas da lista acima.
# a) Intervalo de 1 a 9
# b) Intervalo de 8 a 13
# c) Números pares
# d) Números ímpares
# e) Todos os múltiplos de 2, 3 e 4
# f) Lista reversa
# g) Soma do intervalo de 10 a 15
# h) Uma lista com um novo elemento
# i) Substituir o elemento com índice 6

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# a) Intervalo de 1 a 9
print('a)', lista[1:10])

# b) Intervalo de 8 a 13
print('b)', lista[8:14])

# c) Números pares
print('c)', lista[::2])

# d) Números ímpares
print('d)', lista[1::2])

# e) Todos os múltiplos de 2, 3 e 4
print('e)', [n for n in lista if n % 2 == 0 and n % 3 == 0 and n % 4 == 0])

# f