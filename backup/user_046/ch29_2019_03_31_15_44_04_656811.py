def calcula_aumento(s):
    if s>1250:
       aumento=s*1.1-s
       return (float("{0}".format(aumento)))
    else:
        aumento=s*1.15-s
        return(float("{0}".format(aumento)))