import json

with open ('estoque.json','r') as arq:
    cont=arq.read()
    lista=arq.readlines()

dicio=json.loads(cont)

total=0
i=1
while i<len(lista)-1:
    total+=int(lista[i]['quantidade'])*float(lista[i]['valor'])
    i+=1
print(total)