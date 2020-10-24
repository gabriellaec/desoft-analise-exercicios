with open("palavras.txt","r") as arquivo:
    conteudo = arquivo.read()

li = conteudo.split(" ")

soma =0
i=0
while i<len(li):
    if li[i][0] == 'a':
        soma+=1
       
    elif li[i][0] == 'A':
        soma+=1
    i+=1
    
print (soma)