dicionario = {janeiro:1, fevereiro:2, março:3, abril:4, maio:5, junho:6, julho:7, agosto:8, setembro:9, outubro:10, novemmbro:11, dezembro:12}
nome=input("Nome do mes")
if nome in dicionario:
    print (dicionario[nome])
else:
    print("esse nome nao eh um mes")