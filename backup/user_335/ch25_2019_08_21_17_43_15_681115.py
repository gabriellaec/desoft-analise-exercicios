def PrecoPassagem (d):
    if (d<=200):
        v = d*0.50
        return v
    else:
        v = 100 + ((d - 200)*0.45)
        return v

