a = float(input("Qual o deposito"))
b = float(input("Qual taxa"))
i = 0
s = a
while i <24:
    print ("{0:2d}   {1:.2f}".format(i, s))
    s = s * (1 + (b/100))
    i +=1
	print ("{0:2d}   {1:.2f}".format(i, s))
print(a*(1+b/100)**24)