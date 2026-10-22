# Elaborar um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra.
# Depois o usuário deve digitar um caractere (vogal ou consoante) e o programa deve substituir todas as vogais da palavra dada por esse caractere.

palavra = input('Digite uma palavra: ')
vogais = 'aeiouAEIOUáàãâéêíóôõúÁÀÃÂÉÊÍÓÔÕÚ'
quantidade = sum(1 for letra in palavra if letra in vogais)

print(f'A palavra possui {quantidade} vogais.')

caractere = input('Digite um caractere para substituir as vogais: ')

if len(caractere) == 1:
    nova_palavra = ''.join(caractere if letra in vogais else letra for letra in palavra)
    print(nova_palavra)
else:
    print('Digite apenas um caractere.')