import random
dinheiros = 100
print(dinheiros)
while dinheiros!=0:
    aposta = int(input('aposta '))
    if aposta==0:
        break
    tipo_aposta = input('tipo aposta (n/p) ')
    if tipo_aposta == 'n':
        numero = input('numero ')
        parimpar = '0'
    elif tipo_aposta == 'p':
        parimpar = input('(p/i) ')
    a = random.randint(0,36)
    if parimpar!='0':
        if a == 0:
            dinheiros -= aposta
        elif a%2 ==0:
            if tipo_aposta == 'p':
                dinheiros += aposta
            else:
                dinheiros -= aposta
        else:
            if tipo_aposta == 'i':
                dinheiros += aposta
            else:
                dinheiros -= aposta
    else:
        if numero == 0:
            dinheiros -= aposta
        elif numero == a:
            dinheiros += 35*aposta
        else:
            dinheiros -= aposta
    print(dinheiros)
      