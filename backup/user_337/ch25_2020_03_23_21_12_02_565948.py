from math import sin, radians
v = float(input('v: '))
ao = float(input('ao: '))
pos = (v**2*sin(radians(2*ao))/9.8)
if pos < 98:
    print ('Muito perto')
elif pos >= 98 and pos <= 102:
    print ('Acertou!')
else:
    print ('Muito longe')
    
    
