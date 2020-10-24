def zera_negativos(valores):
    i=0
    valores=[9, -2, 4, -3]
    while i>len(valores):
        if valores[i]<0:
            valores[i]=0
        i=i+1
	print(valores)