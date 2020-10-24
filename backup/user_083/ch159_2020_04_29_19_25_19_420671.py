import json
with open('estoque.json','r') as arquivo:
    conteudo=arquivo.read()
    estoque=json.loads(conteudo)
    conta=0
    for i in estoque['produtos']:
        conta+=i['quantidades']*i['valores']
    print(conta)