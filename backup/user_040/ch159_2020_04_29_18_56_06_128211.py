with open("estoque.json") as arquivo:
    conteudo = arquivo.read()
    valor_total = 0
    for x, y in conteudo.items():
        for z in y:
            if x in z.keys():
                quantidade = z[1]
                valor = z[2]
                valor_total += quantidade*valor
print (valor_total)