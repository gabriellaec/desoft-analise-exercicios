with open ('palavras.txt','w') as texto:

texto = [open('palavras.txt','r')]
palavras=0
palavras_comA=0
vogais_A='aA'

for i in range(len(texto)):
    palavras=texto[i].split()

for i in range(len(palavras)):
    for letra in palavras[i]:
        if letra in vogais_A:
            palavras_comA+=1
            break
print(palavras_comA)
    
arquivo.close()