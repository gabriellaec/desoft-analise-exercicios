import json
with open('estoque.json', 'r') as estoque:
    dic = json.loads(estoque.read())
    soma = 0
    for i in range(len(dic["produtos"])):
        q = dic["produtos"][i]["quantidade"]
        v = dic["produtos"][i]["valor"]
        soma += q*v
print(soma)    
