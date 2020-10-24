lista_palavras= []
a = input(str("palavra:"))

while a != "fim":
    lista_palavras.append(a)
    a = input(str("palavra:"))
    
i = 0
while i < len(lista_palavras):
    b = lista_palavras[i]
    if len(b) > 1 and b[0] == 'a':
        print(b)
    i += 1