with open('churras.txt',encoding="utf8") as arquivo:
    conteudo = arquivo.readlines()
   
lista = list()
l1 = dict() 
for i in conteudo:
    
    a = i.split(',')
    
    lista.append(a)

soma = 0
for t in range(0,len(lista)):
    nome = lista[t][0]
    quantidade =int( lista[t][0+1])
    valor = float( lista[t][0+2])
    soma = soma + quantidade*valor
    #print('O item comprado foi {}, com a quantidade {}, no valor de {}'.format(nome, quantidade, valor))
#print('O valor total da lista é {}'.format(soma))
print(soma)