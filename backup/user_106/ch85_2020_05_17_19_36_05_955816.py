with open ('macacos-me-mordam.txt', 'r') as arq:
    cont=arq.read()
lista=cont.lower().split()
i=0
for palavra in lista:
    if palavra=='banana':
        i+=1
print(i)