def asteriscos(n):
    lista_asteriscos= []
    i= 0
    while i < n:
        lista_asteriscos.append('*')
        i= i + 1
    x= 0
    sequencia_asteriscos= '*'
    while x < n-1:
        sequencia_asteriscos= sequencia_asteriscos + lista_asteriscos[x]
        x= x + 1
        
    return sequencia_asteriscos
