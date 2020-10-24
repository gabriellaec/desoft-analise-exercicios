e=input('Que dia do mês?:')
a=input('Que horas são?:')
b=input('Quantos minutos são?:')
c=input('Quanto segundos são?:')

d=(60*60*24*int(e))+(60*60*int(a))+ (60*int(b)+int(c))
print (d)