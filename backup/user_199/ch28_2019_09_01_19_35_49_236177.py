v=int(input('digite sua velocidade: '))

def multa(v):
    y = (v-80)*5
    if v<=80:
        return 'Não foi multado'
    else:
        return 'Você foi multado em {0} reais'.format(y)   

print (multa(v))
    