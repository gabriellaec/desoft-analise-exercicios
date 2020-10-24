

def imprime_tipo (n):
    if n%3 == 0 and n%5 != 0:
        print('TIPO A')
    elif n%5==0 and n%3!=0:
        print('TIPO B')
    elif n%3==0 and n%5==0:
        print('TIPO C')
    elif n%3!=0 and n%5!=0:
        print('TIPO D')

imprime_tipo(n)
        
        