import json

with open('estoque.json','r') as arquivo_json:
    texto = arquivo_json.read()
    d_estoque = json.loads(texto)
    lista_de_d_produtos = d_estoque['produtos']
    valor = 0
    for d_produto in lista_de_d_produtos:
        valor += d_produto['quantidade'] * d_produto['valor']
        
print (valor)