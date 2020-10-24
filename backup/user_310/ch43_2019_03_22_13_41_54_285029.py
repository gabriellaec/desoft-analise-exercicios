numero= int(input("numero: "))

sequencia=[numero]

numero_inicial= numero

maior_sequencia=0

i=0

while i<=numero_inicial:
    n=sequencia[i]
    if n==1:
        break
    elif n%2==0:
        sequencia.append(n/2)
    else:
        sequencia.append(3*n+1)
    i+=1

print(sequencia)