def calcula_aumento(s):
    if s>1250:
       a=s*1.1-s
       return (float("{0}".format(a)))
    else:
        a=s*1.15-s
        return(float("{0}".format(a)))