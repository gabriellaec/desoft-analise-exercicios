import json
with open('estoque.json', 'r') as arquivo_json:
    texto=arquivo_json.read()
    lista=json.loads(texto)
    t=0
    for i in lista['produtos']:
        t+=i['quantidade']*i['valor']
    print(t)