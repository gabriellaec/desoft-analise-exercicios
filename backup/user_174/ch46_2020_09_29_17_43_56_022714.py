def numero_no_indice(valores):
    valores=[]
    i=0
    while i<int(len(valores)):
        valores[i-1]=i
        i=i+1
        return (valores)
    