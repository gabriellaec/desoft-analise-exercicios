
def calcula_aumento(a):
    y1=a*1.1
    y2=a*1.15
    if a>1250:
        return float('{0:.2f}'.format(y1))
    else:
        return float('{0:.2f}'.format(y2))


    