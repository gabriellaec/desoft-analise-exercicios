i=0
lista_usuario=[float(input('digite um número: '))]
while lista_usuario[i]>0:
    lista_usuario.append(float(input('digite um número: ')))
    i+=1
else:
    del lista_usuario[i]

print(lista_usuario)

j=len(lista_usuario)-1
lista_invertida=[]

while j>=0:
    lista_invertida.append(lista_usuario[j])
    j-=1

print(lista_invertida)