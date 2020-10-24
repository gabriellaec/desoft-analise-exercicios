a = float(input("Qual o deposito"))
b = float(input("Qual taxa"))
i = 0
s = 0
while i <25:
    y = a * (1 + (b/100))**i
    y += s
    i +=1
    print (y)
print(s)
