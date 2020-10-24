def eh_primo(numero) :
    nao_primo = True
    while nao_primo :
        if numero % 2 == 0:
            print('False')
            nao_primo = False

    verdade = True
    a = 1
    while a > numero and verdade:
        if numero % 2 == 0:
            print('Nao é primo')
            verdade = False
        a += 2
    print('é primo')
    return numero