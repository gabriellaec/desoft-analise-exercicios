n=int(input("numero: "))

def calcula_fibonacci(n):
    sequencia=[1, 1]
    i=2
    
    while i<n:
        sequencia.append(sequencia[i-2]+sequencia[i-1])
        i+=1
    return sequencia