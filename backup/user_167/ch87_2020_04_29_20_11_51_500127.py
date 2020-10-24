lista=[]
custo=0
with open( 'churras.txt','r' ) as arquivo:
    arquivo.read()
    lista.append(arquivo)
    for e in range(0, len(lista)):
        custo+=[e[0],len(lista),3]-1
print(custo)
        
    