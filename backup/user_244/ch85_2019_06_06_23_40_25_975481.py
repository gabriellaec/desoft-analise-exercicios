with open('macacos-me-mordam.txt','r') as txt:
    texto = txt.read()
    
t1 = texto.split()
soma = 0 

for i in t1:
    z = i.lower()
    if z == 'banana':
        soma += 1 
        
print(soma)
   
