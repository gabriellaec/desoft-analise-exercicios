def eh_primo(numero) :
    if numero % 2 == 0 :
        print('False')
    i = 1
    a = numero - 2*i
    while numero % 2 != 0 and a > 1 :
        if numero % a == 0 :
            print('False')
        i += 1
        print('True')
    return numero