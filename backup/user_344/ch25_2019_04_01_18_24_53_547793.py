distancia= int(input('Quantos kilometros irá percorrer?'))
if distancia <= 200:
    preço= distancia*0.5
    
else:
    preço= 100 + (distancia - 200)*0.45

print (preço)
   