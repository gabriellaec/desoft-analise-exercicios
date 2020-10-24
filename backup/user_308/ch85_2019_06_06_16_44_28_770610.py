i=0
with open ('macacos-me-mordam.txt') as arq:
    texto=arq.read()

    
texteras=texto.split()
for e in texteras:
    ee=e.upper()
    if ee=='BANANA':
        i+=1
  	
print(i)
            