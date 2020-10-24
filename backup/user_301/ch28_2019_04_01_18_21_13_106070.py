a=float(input('qual velocidade? '))
if a>80:
    m=(a-80)*5
    return ("{0:.2f}".format(m))
else:
    return 'Não foi multado'
 