a=float(input("Depósito inicial?: "))
b=float(input("Taxa de juros?: "))

i=0
s=a
while i < 24:
    s = s + s*(b/100)
    print("%.2f" % s)
    i+=1
    