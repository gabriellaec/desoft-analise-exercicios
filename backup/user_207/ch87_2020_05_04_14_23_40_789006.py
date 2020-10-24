with open ('churras.txt', 'r') as arquivo:
    dados = arquivo.read() #lê todo o conteúdo em uma única string
    primeira_lista = dados.split('\n')
    lista = []
    for elemento in primeira_lista:
        lista.append(elemento.split(','))
    valor =0 
    i=0
    while i<len(lista):
        valor += int(lista[i][1])*float(lista[i][2])
        i+=1
    
print (valor)