d = float(input("depósito inicial: "))
j = float(input("taxa de juros: "))
i = 0
s = d
while i < 24:
    print ("%.2f" % s)
    s = s*(1 + j/100)
    i+=1  
print ("%.2f" % s)