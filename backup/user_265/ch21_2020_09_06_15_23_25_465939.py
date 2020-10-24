d= int (input ('Qantidade de dias: '))
h= int (input ('Quantidade de horas: '))
m= int (input ('Quantidade de minutos: '))
s= int (input ('Quantidade de segundos: '))
def segundos(d,h,m,s):
    y= (d*86400)+(h*3600)+(m*60)+s
    return y
total= segundos(d,h,m,s) 
print (total)