def calcula_tempo(dicionario):
    dic2 = {}
    for k, v in dicionario.items():
        conta  = (200/v)**(1/2)
        dic2[k] = conta
        a = dic2[k]
        nome  = k
        
    for i in dic2:
        if dic2[i] < a:
            nome = i
            a = dic2[i]
    
    resultado = 'O vencedor é {0} com tempo de conclusão de {1} s'.format(nome,a)
    return resultado

dicionario = {}
c = True
while c:
    nome = input('Digite um nome ')
    if nome != 'sair':
        aceleracao = int(input('Digite um valor para a aceleração '))
        dicionario[nome] = aceleracao
        
    elif nome == 'sair':
        c = False
        
print(calcula_tempo(dicionario))    