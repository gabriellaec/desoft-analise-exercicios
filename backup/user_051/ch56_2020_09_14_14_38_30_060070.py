def calcula_norma(lista):
    if len(lista)<=2:
        vetor=((lista[1][0]-lista[0][0])**2 + (lista[1][1]-lista[0][1])**2)**(1/2)
        return vetor
lista=[[6,9], [9,13]]
q=calcula_norma(lista)
print(q)