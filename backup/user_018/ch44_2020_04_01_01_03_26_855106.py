lista1 = [0,1,2,3,4,5,6,7,8,9,10,11,12]
lista2 = ['','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
a = input('Mês = ')
i = 0
for i in range(len(lista2)):
    if a == lista2[i]:
        print(lista1[i])
    i+=1