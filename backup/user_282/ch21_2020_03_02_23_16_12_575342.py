def s(a,b,c,d):
    s = a*3600*24+b*3600+c*60+d
    return s



a=input('quantos dias?: ')
b=input('quantas horas?: ')
c=input('quantos minutos?: ')
d=input('quantos segundos?: ')

print('{0} segundo(s)'.format(s(float(a),float(b),float(c),float(d))))