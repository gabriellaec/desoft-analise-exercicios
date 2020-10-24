distancia= float(input('Qual distância o passageiro deseja percorrer em Km'))

if distancia < 200 or distancia==200 :
    preco= distancia*0.50
if distancia > 200:
    preco= 200*0.50 + ((distancia - 200 )*0.45)
    
print (preco,2)