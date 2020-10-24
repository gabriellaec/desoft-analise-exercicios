a = float(input("Qual o deposito"))
b = float(input("Qual taxa"))
i = 0
s = a
while i <24:
    s = s * (1 + (b/100))
    i +=1
    print ("{0:.2f}".format(s))
