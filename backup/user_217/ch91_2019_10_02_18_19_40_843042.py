f = open('palavras.txt', "r")
contador = 0
x=f.read()
for line in x:  
    if line == 'a' line == 'A':
        contador+=1
print(contador)
    
f.close()     