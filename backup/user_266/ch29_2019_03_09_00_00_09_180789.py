def calcula_aumento(s):
    if s > 1250:
        s = s*1.1
        return (float('{0}'.format(s)))
    else:
        s = s*1.15
        return (float('{0}'.format(s)))