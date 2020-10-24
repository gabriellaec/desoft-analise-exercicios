def segundos_entre(valor_string1,valor_string2):
    x=valor_string1-valor_string2
    return x

string1=('hh:mm:ss')
a=(string1.find(hh))*60*60
b=(string1.find(mm))*60
c=string1.find(ss)
valor_string1= a+b+c

string2=('hh:mm:ss')
d=(string2.find(hh))*60*60
e=(string2.fin(mm))*60
f=string2.find(ss)
valor_string2= d+e+f