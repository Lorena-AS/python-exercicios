# 3) Elaborar um programa que leia uma lista com 4 números reais,
# em seguida o programa deve exibir as notas e a média.

notas = []

for i in range(4):
    while True:
        try:
            nota = float(input(f'Digite a {i + 1}ª nota: '))
            notas.append(nota)
            break
        except ValueError:
            print('Entrada inválida! Digite um número real.')

media = sum(notas) / len(notas)

print('Notas:', notas)
print(f'Média: {media:.2f}')