i=1
contador=0
maior=0
resposta=0

while i<1000:
    while i!=1:
        contador+=1
        elif i%2==0:
            i=i/2
        else:
            i=3*i+1
    if contador>maior:
        maior=contador
        resposta=i
    i+=1

print(resposta)