def eh_bissexto (ano):
    ano = int(input('digite um numero: '))
    if ano==1 or ano%4==0 or ano%100!=0:
        return True
    else:
        return False