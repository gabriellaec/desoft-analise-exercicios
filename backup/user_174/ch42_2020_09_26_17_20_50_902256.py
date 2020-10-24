lista_palavra=[]
palavra=input("Que palavra?")
while palavra !='fim':
    lista_palavra.append(palavra)
    palavra=input("Outra plavra?")
#Imprime outra palavra que começa com 'a'.
i=0
while i<len(lista_palavra):
    palavra=lista_palavra[i]
    if len(palavra)>1 and palavra[0]=='a'
        print(palavra)
i=i+1