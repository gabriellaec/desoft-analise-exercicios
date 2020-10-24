z = "10:25:00"
x = "11:00:00"
def segundos_entre(z,x):    
    somatotal = 0
    p = x[0:2]
    int(p)
    a = z[0:2]
    int(a)
    b = x[3:5]
    int(b)
    c = z[3:5]
    int(c)
    d = x[6: ]
    int(d)
    e = z[6: ]
    int(e)
    
    somatotal = (int(p)-int(a))*3600 + (int(c)-int(b))*60 + (int(d)-int(e))
    return somatotal
print(segundos_entre(z,x))