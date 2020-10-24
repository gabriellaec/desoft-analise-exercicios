def calcula_fibonacci(n):
    if n==1:
        return [1]
    sequencia=[1, 1]
    i=2
    
    while i<n:
        sequencia.append(sequencia[i-2]+sequencia[i-1])
        i+=1
    return sequencia