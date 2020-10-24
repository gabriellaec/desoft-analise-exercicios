def total (a, b, c ,d):
    t = a*86400 + b*3600 + c*60 + d
    return t

dia = int(input("Digite quantos dias:" ))
hora = int(input("digite quantas horas:" ))
minutos = int(input("digite quantos minutos:" ))
segundos = int(input("digite quantos segundos:" ))

tot = total(dia, hora, minutos, segundos)
print (tot)