seqant=0
seqatual=0
numero = 0
n=4
j=n
while n<1000:
    while j!= 1:
        if j%2==0 and n!=1:
            j = j /2
            seqatual+=1

        elif n!=1:
            j=3*j+1
            seqatual+=1

    if seqatual>seqant:
        seqant=seqatual
        numero = n
        n+=1
        j=n
        seqatual=0
    else:
        n+=1
        j=n
        seqatual=0
print(numero)