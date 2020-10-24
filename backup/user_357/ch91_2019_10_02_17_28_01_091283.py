with open ('palavra.txt' , 'r') as arquivo:
    conteudo = arquivo.read()
    


lista = str.split(conteudo)

i = 0 
palavra_começa_a = 0 

while i < len(lista): 
    if lista[i][0] == 'a' or lista[i][0] == 'A': 
        palavra_começa_a += 1 
    i+= 1 
    
    
print(palavra_começa_a)