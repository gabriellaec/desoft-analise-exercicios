import json

with open ('estoque.json','r') as arq:
    cont=arq.read()

dicio=json.loads(cont)
listap=dicio['produtos']

total=0
for minidic in listap:
    total+=int(minidic['quantidade'])*float(minidic['valor'])
    
print(total)