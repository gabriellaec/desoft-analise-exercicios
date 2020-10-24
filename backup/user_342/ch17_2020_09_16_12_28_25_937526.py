def eh_bissexto(x):
    ano=365+0,25*x
    x=x+1
    if x==366:
        print ('bissexto')
    if x<366:
        print ('nao_eh_bissexto')
    
