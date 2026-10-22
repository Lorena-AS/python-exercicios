# Escreva um programa que verifique se uma frase é um palíndromo.

print('Sua palavra é um palíndromo?')
p = input('Digite uma palavra: ').lower().strip()
invertido = ''

for i in range(len(p)-1, -1, -1):
    invertido = invertido + p[i]

print(f'A palavra invertida é: {invertido}')

if invertido == p:
    print('Sua palavra é um palíndromo!')
else:
    print('Sua palavra não é um palíndromo.')
