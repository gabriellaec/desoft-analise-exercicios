som = 0
soma = []
a = int(input('Digite um número: '))
soma.append(a)

while a != 0:
    a = int(input('Digite um número: '))
    soma.append(a)
    
for i in soma:
    som += soma[i]
print(som)