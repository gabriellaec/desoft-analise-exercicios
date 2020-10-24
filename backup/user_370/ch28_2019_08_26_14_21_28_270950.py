v=float(input('Qual foi a sua velocidade'))
if v<=80:
        print('Não foi multado')
elif v>80:
        multa=(v-80)*5
        print('A multa foi de {0:.2f}'.format(multa)) 
        
        