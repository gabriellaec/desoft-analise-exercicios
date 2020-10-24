def preco(dist):
    if dist <= 200:
        p = dist*0.5
        return p
    else:
        p =  dist*0.45
        return p
pre =preco(int(input("Digite a distância ")))
print ("%.2f"%(pre))