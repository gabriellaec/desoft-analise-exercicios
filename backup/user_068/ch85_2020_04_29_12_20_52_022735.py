with open('macacos-me-mordam.txt', "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
s = 0
for palavra in lista:
    if palavra.lower() == 'banana':
        s += 1
print(s)
        