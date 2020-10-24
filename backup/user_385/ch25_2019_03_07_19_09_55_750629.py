def preco(d):
    if d<200:
        return d*0.50
    else:
        return 100+d*0.45
    
d= int(input('distancia?'))
print (preco(d))
      