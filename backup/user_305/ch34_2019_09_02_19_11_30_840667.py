a = float(input("Qual o deposito"))
b = float(input("Qual taxa"))
i = 0
while i <24:
    y = a * (1 + (b/100))**i
    i +=1
print (y)