Rodando= True
while Rodando:
    a=int(input('Digite um número'))
    contador=0
    if a!=0:
        a=int(input('Digite um número'))
        contador+=a
        contador+=1
    else:
        Rodando= False
        print (contador)
