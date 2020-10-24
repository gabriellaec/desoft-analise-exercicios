lista = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
i = 0
a = str(input('Mês = '))
while i < 12:
    if a == lista[i]:
        print(i+1)
    i+=1