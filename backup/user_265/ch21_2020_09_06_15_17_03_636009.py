d= input ('Qantidade de dias: ')
h= input ('Quantidade de horas: ')
m= input ('Quantidade de minutos: ')
s= input ('Quantidade de segundos: ')
def segundos(d,h,m,s):
    y= (d*86400)+(h*3600)+(m*60)+s
    return y
total= segundos(d,h,m,s) 
print total