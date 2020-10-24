velocidade_do_carro_do_usuario = int(input('Qual era a velocidade do carro? '))
if velocidade_do_carro_do_usuario > 80 :
    def multa(velocidade) :
        valor_da_multa=(velocidade - 80)*5
        return valor_da_multa
    a = multa(velocidade_do_carro_do_usuario)
    print('O usuario ira pagar {0:.2f} reais de multa'.format(a))
else:
    print('Não foi multado')

