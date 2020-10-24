palavras=[]
palavra=input('Digite uma palavra: ')
while 'fim' != palavra:
    palavras.append(palavra)
    palavra=input( 'Digite uma palavra: ') 
i=0
while i< len(palavras) :
    palavra=palavras[i]
    if palavra[0]== 'a' or palavra[0]=='A': 
            print(palavras[i]) 
    i+=1 
    
