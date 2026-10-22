# Elaborar um programa que receba do usuário uma string. O programa deve imprimir a string sem suas vogais.

texto = input('Digite uma string: ')
vogais = 'aeiouáàãâéêíóôõúüAEIOUÁÀÃÂÉÊÍÓÔÕÚÜ'

resultado = ''.join(letra for letra in texto if letra not in vogais)

print(resultado)