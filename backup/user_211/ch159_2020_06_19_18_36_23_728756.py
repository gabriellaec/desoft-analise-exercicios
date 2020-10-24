import json
total=0
with open('estoque.json','r') as arquivo:
    conteudo = arquivo.read()
    dic = json.loads(conteudo)    #teremos um dicionario com uma listra de dicionarios
for i in range(0,len(dic['produtos'])): #percorreremos cada dicionario dessa lista de dicionarios  
    dic['produtos'][i]["preco_total"] = dic['produtos'][i]['quantidade']*dic['produtos'][i]['valor']#a cada dicionario dessa lista de dicionarios estou adicionando uma nova key chamada valor total que multiplica a quantidade de produtos pelo preço
    total+=dic['produtos'][i]["preco_total"] #aproveitando que ta percorrendo a lista de dic, somando os values da nova key criada, dá o valor total da porra toda
print(total)
