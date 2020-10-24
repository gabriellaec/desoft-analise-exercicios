executando=True
while executando:
    pergunta = input("codigo esta executando (s/n): ")
    if pergunta == 's':
        produz = input('produx o resultado correto? (n/s):')
        executando = True
        if produz == 's':
            print('parabens')
        else:
            executando = False 
    else:
        tem_duvida = False