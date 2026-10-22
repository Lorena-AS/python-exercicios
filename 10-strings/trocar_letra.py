# Elaborar um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string.
# A string e as letras L1 e L2 devem ser fornecidas pelo usuário.

texto = input('Digite uma string: ')
l1 = input('Digite a letra que deseja substituir: ')
l2 = input('Digite a nova letra: ')

if len(l1) == 1 and len(l2) == 1:
    resultado = texto.replace(l1, l2)
    print(resultado)
else:
    print('Digite apenas uma letra em cada campo.')