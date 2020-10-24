a = int (input ('Velocidade do usuário: '))
def multa(a):
    if a > 80:
        print ('Foi multado em {0:.2f}' .format ((a-80)*5))
    else:
        print ('Não foi multado')