import math
 
def calcula_tempo(l1):
    dicionario = {}
    
    for k, v in l1.items():
        tempo = math.sqrt(200/v)
        dicionario[k] = tempo
        a = dicionario[k]
        nome = k
    
    
 
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