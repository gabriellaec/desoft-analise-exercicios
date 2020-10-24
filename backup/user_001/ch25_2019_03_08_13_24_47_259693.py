def preco_passagem(n):
    
    if n <= 200:
        return (n*0.5)
    return (((n-200)*0.45)+100)