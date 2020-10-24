with open('texto.txt', 'r') as arquivo:
    conteudo=arquivo.read()
palavra=conteudo.split()

i=0
while i<len(palavra):
    i+=palavra[i]
    i+=1

        
    

    