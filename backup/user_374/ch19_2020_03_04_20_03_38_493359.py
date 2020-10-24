def triangulos(x,y,z):
    if (x==y and x==z):
        return "equilátero"
    elif x!=y and x!=z:
        return "escaleno"
    else:
       return "isóceles"
print(triangulos(2,1,1))
    
