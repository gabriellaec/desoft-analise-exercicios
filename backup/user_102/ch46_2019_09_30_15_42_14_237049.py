lista_palavras= []
a = input(str("palavra:"))

while a != "fim":
    lista_palavras.append(a)
    a = input(str("palavra:"))
    
i = 0
while i>len(lista_palavras):
    a = lista_palavras[i]
    if len(a) > 1 and a[0] == 'a':
        print(a)
    i += 1