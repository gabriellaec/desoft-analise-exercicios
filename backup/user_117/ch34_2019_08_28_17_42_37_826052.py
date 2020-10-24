d = float(input("deposito inicial: "))
j = float(input("taxa de juros: "))

i = 0

while i < 23:
    t = d + (1 + j) ** i
    i+=1
    print ('{:.2f}'.format(t))