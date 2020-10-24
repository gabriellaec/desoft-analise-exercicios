deposito_inicial=float(input('qual é o seu depósito inicial?   :'))
taxa_de_juros=float(input('e a taxa de juros?  :'))
def ganho_com_juros(capital_inicial):
    for tempo in range(1,25):
    y=deposito_inicial*((1+taxa_de_juros)**tempo)
    return y
print('seu ganho total no mês {0}, é de {1}'.format(tempo,y))

    
    