
lista1 = [0,1,2,3,4,5,6,7,8,9,10,11,12]
lista2 = ['','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
a = input('Mês = ')
for i in range(len(lista1)):
    if a == lista1[i]:
        print(lista2[i])