import json
total=0
with open('texto.json','r') as arquivo:
    conteudo = arquivo.read()
    dic = json.loads(conteudo)
for i in range(0,len(dic['produtos'])):   
    dic['produtos'][i]["preco_total"] = dic['produtos'][i]['quantidade']*dic['produtos'][i]['valor']
    total+=dic['produtos'][i]["preco_total"]
print(total)
