n=1000
dividendo=0
contador=0
maior_arvore=0
while n!=0:
    dividendo=n
    while dividendo!=1:
    	if dividendo%2==0:
        	dividendo=dividendo/2
        else:
            dividendo=3*dividendo+1
        contador=contador+1
    maior_arvore=contador
    n=n-1
print(maior_arvore)