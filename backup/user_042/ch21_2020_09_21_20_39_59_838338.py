diga_dia = int(input('Me dê um dia'))
diga_hora = int(input('Me dê um hora'))
diga_minuto = int(input('Me dê um minuto'))
diga_segunda = int(input('Me dê um segundo'))

d = diga_dia*24*60*60
h = diga_hora*60*60
m = diga_minuto*60

print(d+h+m+diga_segunda)