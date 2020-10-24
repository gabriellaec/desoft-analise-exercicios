def calcula_total_da_nota(lista1,lista2):
    nota_fiscal=[]
    parte1=[]
    parte2=[]
    for produtos in lista1:
        for quantidade in lista2:
            parte1.append(produtos)
            parte2.append(quantidade)
            nota_fiscal = parte1 + parte2
    return (nota_fiscal)
   