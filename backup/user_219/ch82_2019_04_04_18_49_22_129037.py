
palavra= input('digite uma palavra')
def primeiras_ocorrencias(palavra):
    saída= []
    for i in palavra:
        if i in saída:
            saída[i]+=1