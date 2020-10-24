with open ('palavras.txt','w') as texto:

s=0
for letra in texto:
    if letra in 'aA':
        s=s+1       
print(s)