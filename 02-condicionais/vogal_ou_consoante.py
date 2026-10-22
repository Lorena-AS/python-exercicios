# Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

try:
    letra = input('Digite uma letra: ').strip().lower()

    if len(letra) != 1 or not letra.isalpha():
        print('Entrada inválida! Digite apenas uma letra.')
    elif letra in 'aáàãâeéèêiíìîoóòõôuúùû':
        print('Sua letra é uma vogal.')
    else:
        print('Sua letra é uma consoante.')

except (ValueError, IndexError):
    print('Entrada inválida!')