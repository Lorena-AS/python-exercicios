# Elaborar um programa que leia um nome e imprima o nome somente se a
# primeira letra do nome for “a” ou “e” (maiúscula ou minúscula).

nome = input('Digite seu nome: ').strip()

if nome and nome[0].lower() in ['a', 'e']:
    print(nome)