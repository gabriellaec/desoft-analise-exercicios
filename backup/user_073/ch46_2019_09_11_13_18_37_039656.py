palavras=[]
palavra=input('digite...')
while 'fim'!=palavra:
    palavras.append(palavra)
    palavra=input('digite...')
i=0
while i<len(palavras):
    palavra=palavras[i]
    if palavra[0]=='a' or palavra[0]=='A':
        print(palavra)
    i+=1