from googletrans import Translator

dia=int(input('a '))
a=calendar.month_name[dia]
b=Translator(a)

print (b.translate(a,dest='pt'))
