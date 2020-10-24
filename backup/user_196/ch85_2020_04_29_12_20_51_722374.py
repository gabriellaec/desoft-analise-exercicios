quantidade = 0
with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
for linha in lista:
    if palavra.upper() == "BANANA":
        quantidade+=1
print(quantidade)