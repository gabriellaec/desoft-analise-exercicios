lista2 = ['','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
a = input('Mês = ')
i = 0
while i < len(lista2):
    if a == lista2[i]:
        print(i)
    i+=1