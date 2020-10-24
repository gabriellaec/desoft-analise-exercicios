from math import sqrt
 
def calcula_tempo(dic):
    dicionario = {}
    for i in dic:
        v = sqrt(2*100*dic[i])
        t = v / dic[i]
        if t not in dicionario:
            dicionario[i] = t
            
    return dicionario
    
    
 
    for i in dicionario:
        if dicionario[i]<a:
            nome = i
            a = dicionario[i]
        
    resultado = 'O vencedor é {} com tempo de conclusão de {} s'.format(nome,a)
 
    return resultado
 
dicionario = {}
while True:
    nome = str(input('Digite o nome do corredor: '))
    if nome == 'sair':
        break
 
    aceleração = float(input('Digite a aceleração: '))
 
    dicionario[nome] = aceleração
 
print(calcula_tempo(dicionario))