d = int(input(distancia))
def preco_passagem(d):
    if d<=200:
        p=d*0.5
	else:
        p=(d-200)*0.45+100
    return p
