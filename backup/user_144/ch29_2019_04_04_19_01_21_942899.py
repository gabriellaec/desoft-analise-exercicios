def calcula_aumento(sal):
    for k in sal:
        if sal > 1250:
            sal = sal+sal*0.1
        for k1 in sal:
            if sal <= 1250:
                sal = sal+sal*0.1
                return sal 

