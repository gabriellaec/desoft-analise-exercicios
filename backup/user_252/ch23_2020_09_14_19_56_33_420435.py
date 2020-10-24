v=float(input('Qual velocidade: '))
if v>80:
    a=(v-80)*5
    print('Você foi multado, {0:.2f} reais'.format(a))
elif v<80:
    print('Não foi multado')
    
        
