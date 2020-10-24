#Com o while
i = 0
soma = 0

while i < 100:
    soma = soma + (1/(soma**i))
    i += 1
print(soma)

#Com o for
i = 0
soma = 0 

for i in range(100):
    soma = soma + (1/soma**i)
    i += 1
    
print(soma)