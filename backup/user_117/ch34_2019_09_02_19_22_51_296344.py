d = float(input("depósito inicial: "))
j = float(input("taxa de juros: "))

i = 0
while i < 24:
    v = d*(1 + j/100)**i
    i+=1  
    print ("%.2f" % v)