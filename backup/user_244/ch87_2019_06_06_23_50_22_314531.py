with open('churras.txt','r') as churras:
    texto = churras.read()
custo = 0    
for i in texto:
    quant = float(i[1])
    preco = float(i[2])
    custo += quant*preco
    
print(custo)