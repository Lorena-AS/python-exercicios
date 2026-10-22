print("""TABELA DE LANCHES
      100 = CACHORRO QUENTE | R$ 3,50
      101 = BAURU SIMPLES | R$ 3,80
      102 = BAURU C/ OVO | R$ 4,50
      103 = HAMBURGER | R$ 4,70
      104 = CHEESEBURGER | R$ 5,30
      105 = REFRIGERANTE | R$ 4,00""")

codigo = int(input("Informe o código do item: "))
quantidade = int(input("Qual a quantidade? "))

if codigo == 100:
    valor = quantidade * 3.50
elif codigo == 101:
    valor = quantidade * 3.80
elif codigo == 102:
    valor = quantidade * 4.50
elif codigo == 103:
     valor = quantidade * 4.70
elif codigo == 104:
    valor = quantidade * 5.30
elif codigo == 105:
    valor = quantidade * 4.00
else:
    print("Código não existe")

print(f"O valor do seu lanche é R${valor}")