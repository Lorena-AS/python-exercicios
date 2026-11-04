# Crie uma lista com textos e número. Mostre apenas os textos, em letras maiúsculas.
# Utilize ISINSTANCE

coisas = ["sol", 1032, 1591, "girassol", 50.0, "jardim", 12, "suculenta"]
resposta = []
for item in coisas:
    if isinstance(item, str):
        resposta.append(item.upper())
print(resposta)
