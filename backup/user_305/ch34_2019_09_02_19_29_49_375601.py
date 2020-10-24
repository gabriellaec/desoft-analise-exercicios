a = float(input("Qual o deposito"))
b = float(input("Qual taxa"))
i = 0
s = 0
while i <24:
    y = a * (1 + (b/100))**i
    s += y
    i +=1
    print ({0:.2f}.format(y))
print({0:.2f}.format(s))
