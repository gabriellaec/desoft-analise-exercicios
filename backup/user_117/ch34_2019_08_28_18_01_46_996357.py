d = float(input("deposito inicial: "))
j = float(input("taxa de juros: "))

i = 0
t = d
while i < 24:
    #t = d + (1 + (j/100)) ** i
    t = t * (1+j/100)
    i+=1
    print ('{:.2f}'.format(t))

print('{:.2f}'.format(t-d))    