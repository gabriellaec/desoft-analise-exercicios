lista=[]
n=continuar
i=0
while n==continuar:
    palavra=input("digite uma palavra")
    lista.insert(palavra)
    n=input("continuar a digitar?(continuar/fim)")
while i<len(lista)+1:
    pri_letra(i)=lista[0]
    if pri_letra(i)=='a':
        print(pri_letra(i))
        i+=1
    
    
    
    