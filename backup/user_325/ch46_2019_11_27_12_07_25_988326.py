lista_palavras= []
a = input(str("palavra:"))

while a != "fim":
    lista_palavras.append(a)
    a = input(str("palavra:"))
    i = 0
	
for e in lista_palavras:
    if e[0] == 'a':
        print(e)