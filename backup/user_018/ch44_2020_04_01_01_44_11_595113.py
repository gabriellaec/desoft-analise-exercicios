lista = ['','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
a = str(input('Mês = '))
i = 0
while i < 12:
    if a == lista[i]:
        print(i+1)
    i+=1