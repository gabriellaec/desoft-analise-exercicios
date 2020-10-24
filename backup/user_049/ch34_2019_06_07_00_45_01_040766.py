deposito = float(input('deposito: '))
taxa = float(input('taxa: '))

i = 1
taxa += 1

while i<25:
    n = deposito*taxa**i
    i+=1
    print('{:.2f}'.format(n))
    
s = n-deposito    
print('{:.2f}'.format(s))