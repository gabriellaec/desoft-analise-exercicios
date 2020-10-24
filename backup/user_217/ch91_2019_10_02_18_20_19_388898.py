f = open('palavras.txt', "r")
contador = 0
x=f.read()
for line in x:  
    if line == 'a' or line == 'A':
        contador+=1
f.close()     
print(contador))     