inicial=float(input('deposito inicial'))
taxa=float(input('taxa de juros'))
taxa+=1
depositos= inicial
mensal=float(input('deposito mensal'))
montante=inicial*taxa
montante+=mensal
depositos+=mensal
print('poupança no mês {} é {:.2f}'.format(1,montante))
i=2
while i<=24:
    montante=montante*taxa
    mensal=float(input('deposito mensal'))
    montante+=mensal
    depositos+=mensal
    print('poupança no mês {} é {:.2f}'.format(i,montante))
    i+=1
print(montante-depositos)
    
    

    
        