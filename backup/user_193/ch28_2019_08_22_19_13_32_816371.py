v=int(input('Qual a velocidade do seu carro? '))

def multa(a):
    if v<=80:
        return 'Não foi multado'
    else:
        return 'Voce foi multado em R$ {0:.2f}'.format( (v-80)*5)
    
print (multa(v))