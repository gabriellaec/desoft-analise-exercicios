def preco(x):
    if (x<=200):
        p= x*0.50
        return p
    else:
        r= (200*0.50)+((x-200)*0.45)
        return r
    
custo = float(input("Qual a distância que você irá percorrer? "))
print(preco(custo))