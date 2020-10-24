palavras =[]
t= True
while t:
    palavra = input("Digite uma palavra")
    if palavra !="fim":
        if palavra [0]!="a":
            pass
        else:
            palavras.append(palavra)
    else:
        break 
linha = 0
while linha< len(palavras):
    print(palavras [linha])
    linha+=1
    
        
        