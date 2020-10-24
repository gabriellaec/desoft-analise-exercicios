def preco(km):
    if km<=200:
        return (km*0.5)
    else :
        return (km*0.5+0.45*km)
c=preco(float(input('digite a disttania a ser percorrida')))
print(c)