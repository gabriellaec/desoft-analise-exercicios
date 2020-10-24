def segundos(a,b,c,d):
    S=(a*86400)+(b*3600)+(c*60)+(d)
    return(S)

a=int(input("quantos dias?"))    
b=int(input("quantas horas?"))
c=int(input("quantos minutos"))
d=int(input("quantos segundos?"))
print(segundos(a,b,c,d))