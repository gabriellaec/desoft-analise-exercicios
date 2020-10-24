i=1
j=1
mult=1
div= 1
lista=[]
def PiWallis(n):
    while i < n:
        mult*=(2*i)
        div*=((2*i)-1) 
        a= mult/div
        lista.append(a)
    while j < n:
        mult2*=(2*i)
        div2*= ((2*i)+1)
        b= mul2/div2
        lista.append(b)

resultado = numpy.prod(lista)
return resultado
                    
        
        
    