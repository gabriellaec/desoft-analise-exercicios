with open("churras.txt", "r")as arq:
    conteudo=arq.read().split()
    valor=0
    for i in range (1, len(conteudo)-1, 2):
        valor+=conteudo[i]*conteudo[i+1]
print (valor)
        
    