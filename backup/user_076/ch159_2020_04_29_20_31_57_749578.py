with open('estoque.json','r') as arquivo_json:
    d_estoque = arquivo_json.read()
    valor = 0
    for d_produto in d_estoque:
        valor += d_produto['quantidade'] * d_produto['valor']
        
print (valor)