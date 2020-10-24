import random 
caixa=100
aposta=1
while(caixa>0 and aposta!=0):
    sorteio=random.randint(0,36)
    tipo_aposta=input('n ou paridade')
    if(tipo_aposta=='n'):
        aposta=int(input('diga o valor da sua aposta'))
        if(aposta==sorteio):
             caixa+=35*aposta
        else:
            caixa-=aposta
    if(tipo_aposta=='paridade'):
        aposta==roleta
        par_impar=input('diga se é p ou i')
        if(par_impar=='i' and aposta%2!=0 or par_impar=='p' and aposta%2==0):
            caixa+=aposta
        else:
            caixa-=aposta
print('voce tem em caixa R$',caixa)
print ('fim do jogo')        
    