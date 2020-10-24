quantidade = 0
with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
for linha in lista:
    for palavra in lista:
        if palavra.upper() == "banana":
            quantidade+=1
print(quantidade)