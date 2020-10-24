v=int(input('velocidade'))
if v=<80:
    print('Não foi multado')
else:
    def multa(v):
        y=(v-80)*5
        return y
    print('o valor da multa foi {:.2f}'.format(multab(v)))
    