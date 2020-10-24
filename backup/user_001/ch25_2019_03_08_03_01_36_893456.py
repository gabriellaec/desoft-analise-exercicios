def preco_passagem():
    
    n=int(input("digite a distancia em km:"))
    if n <= 200:
        return (n*0.5)
    return (((n-200)*0.45)+100)

print(preco_passagem())