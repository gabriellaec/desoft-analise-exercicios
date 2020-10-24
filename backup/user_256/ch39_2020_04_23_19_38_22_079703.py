numero = int(input("Digite um numero: "))
n = numero
sequencia = [numero]
mais_longa = sequencia
while numero < 1000:
    while n !=1:
        if n%2 == 0:
            n = n/2
            sequencia.append(n)
        if n%2 !=0:
            n = n*3 +1
            sequencia.append(n)
    if len(sequencia)>len(mais_longa):
        mais_longa = sequencia
    numero = int(input("Digite um numero: "))
    n = numero
print (mais_longa)
    
    