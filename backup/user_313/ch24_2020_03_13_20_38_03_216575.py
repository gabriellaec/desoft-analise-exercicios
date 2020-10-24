def calcula_aumento (a):

    if (a > 1250):
        return('%.2f' %(a*0.1))

    elif (0 < a < 1250):
        return('%.2f' %(a*0.15))

print(calcula_aumento(0.5))


