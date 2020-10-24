def calcula_aumento(s):
    if s > 1250:
        s = s*1.1-1250
        return (float('{0}'.format(s)))
    else:
        s = s*1.15-s
        return (float('{0}'.format(s)))