# Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

print('Reajuste Salarial')
salario = float(input('Informe o seu salário bruto: R$ '))

porcentagem = salario * 0.60
reajuste = salario + porcentagem

print(f'O salário de R$ {salario:.2f} com o reajuste positivo de 60% será de R$ {reajuste:.2f}.')
