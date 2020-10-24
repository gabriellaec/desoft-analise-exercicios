import math

form = []
trig = []
sub = []

i = 0
while i<91:
    x = 4*i*(180 - i)/(40500 - i*(180 - i))
    form.append(x)
    
    ang = math.radians(i)
    y = math.sin(ang)
    trig.append(y)
    
    sub.append(form[i] - trig[i])
    
print(max(sub))
