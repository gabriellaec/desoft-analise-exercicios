sb= float(input('valor: '))
dp= float(input ('dependentes: '))

if sb<= 1045.00:
    inss= sb * 0.075
elif sb> 1045.00 and sb<= 2089.60:
    inss= sb* 0.09
elif sb> 2089.60 and sb <= 3134.40:
    inss= sb* 0.012
elif sb> 3134.40 and sb <= 6101.06:
    inss= 671.12
else:
    inss= sb* 0.014

base= sb- inss -dp*189.59

if base<= 1903.98:
    t= 0
elif base> 1903.98 and base<= 2828.65:
    t= 0.075* base - 142.8
elif base> 2826.65 and base<= 3751.05:
    t= base*0.15 - 354.8
elif base> 3751.05 and base<= 4664.68:
    t= base* 0.225 - 636.13
else:
    t= base* 0.275- 869.36

print (t)
    