def segundos(a,b,c,d,e):
    S=(a*31536000)+(b*2628000)+(c*86400)+(d*3600)+(e)
    return(S)
a=int(input('qantos anos?'))
b=int(input("quantos meses?"))
c=int(input("quantos dias?"))    
d=int(input("quantas horas?"))
e=int(input("quantos segundos?"))
print(segundos(a,b,c,d,e))