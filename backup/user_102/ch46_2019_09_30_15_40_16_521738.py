lista_palavras= []
a = input(float("palavra:"))

while a != "fim":
    lista.palavras.append(a)
    a = input(float("palavra:"))
    
i = 0
while i>len(lista_palavras):
    a = lista_palavras[i]
    if len(a) > 1 and a[0] == 'a':
        print(a)
    i += 1