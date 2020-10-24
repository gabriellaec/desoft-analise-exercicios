lista_palavra=[]
palavra=input('Palavra?: ')
while palavra!='fim':
    lista_palavra.append(palavra)
    palavra=input('Outra palavra: ')
i=0
while i<len(lista_palavras):
    palavra=lista_palavra[i]
    if len(palavra)>1 and palavra[0]=='a':
        print(palavra)
    i=i+1