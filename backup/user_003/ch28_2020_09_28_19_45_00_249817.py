x=2
soma=0
elevado = 0
for x in range(1,100):
    soma += 1/x
    x = x**elevado
    elevado +=1

print(x) 