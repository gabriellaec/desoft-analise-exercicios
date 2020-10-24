with open("texto.txt", "r") as arquivo:
    conteudos = arquivo.read()
lista = conteudos.split()
print(len(lista))