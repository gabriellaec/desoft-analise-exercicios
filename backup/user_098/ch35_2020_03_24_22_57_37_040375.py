Rodando= True
contador=0

while Rodando:
    a=int(input('Digite um número'))
    if a!=0:
        contador+=a
    else:
        Rodando= False
        print (contador)