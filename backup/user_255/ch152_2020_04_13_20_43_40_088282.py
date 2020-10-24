def verifica_preco(catalogo,compras):
    valor_total=0.0
    for item in compras:
        if item in catalogo:
            valor_total+=catalogo[item]
    return valor_total
catalogo={"Pinóquio": 20.0, "Dom Quixote": 40.0, "O Pequeno Príncipe": 10.0}
compras=[]
produto=input('Qual o nome do livro?   ')
if produto in catalogo:
    compras.append(produto)
else:
    print ('Este produto nao existe!')
total=verifica_preco(catalogo,compras)