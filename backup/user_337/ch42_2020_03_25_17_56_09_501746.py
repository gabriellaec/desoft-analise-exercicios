lista_p = []
p = input('dig palav')
while p != 'fim':
    lista_p.append(p)
    p = input('outra palav')

i = 0
while i < len(lista_p):
    p = lista_p[1]
    if len(palavra) > 1 and palavra[1] == "a":
        print(p)
    i += 1
	