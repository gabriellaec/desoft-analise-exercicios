def soma_valores(valores):
    s=0
    i=0
    while i<len(valores):
        s+=valores[i]
        i+=1
        return s
v=[2,4,6,8]
resultado=soma_valores(v)
print (resultado)
    