def sem_problemas():
    print('Sem problemas!')

resposta1 = str(input('O programa está funcionando? [s/n]'))
if resposta1 == 's':
    sem_prbolemas()
else:
    resposta2 = str(input('Você sabe corrigir? [s/n]'))
    if resposta2 == 's':
        sem_prbolemas()
    else:
        resposta3 = str(input('Você precisa corrigir? [s/n]'))
        if resposta3 == 's':
            sem_prbolemas()
        else:
            print('Apague tudo e tente novamente')