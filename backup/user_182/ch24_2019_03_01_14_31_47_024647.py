print("Equilátero, isósceles ou escaleno?")
a=int(input("qual o tamanho do primeiro lado?"))
b=int(input("qual o tamanho do segundo lado?"))
c=int(input("qual o tamanho do terceiro lado?"))

def tipodetriangulo(x,y,z):
    if x==y and y==z:
        return "equilátero"
    elif x!=y or y!=z or x!=z:
        return "isosceles"
    else:
        return "escaleno"
r=tipodetriangulo(a,b,c)
print(r)
