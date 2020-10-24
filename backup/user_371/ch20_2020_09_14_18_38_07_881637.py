def preco(dist):
    if dist <= 200:
        p = dist*0.5
        return p
    else:
        p =  dist*0.45
        return p
print(preco(int(input("Digite a distância "))))