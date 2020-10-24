i=0
contador=0
maior=0
resposta=0

while i<1000:
    while True:
        contador+=1
        if i==1:
            break
        elif i%2==0:
            i=i/2
        else:
            i=3*i+1
    if contador>maior:
        maior=contador
        resposta=i
    i+=1

print(resposta)