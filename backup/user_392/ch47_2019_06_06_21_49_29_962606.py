mes = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
n = int(input('digite um número de mes:'))

i = 0 

while i < len(mes):
    if n == i:
        print(mes[i-1])
    i += 1