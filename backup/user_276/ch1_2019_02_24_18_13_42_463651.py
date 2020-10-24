def calcula_valor_devido(v_emp,meses,txa_juros):
    b = v_emp * (1 + txa_juros)**meses
    return b
v_emp = 3000
meses = 4
txa_juros = 10
a = calcula_valor_devido(3000, 4,10)
print(a)