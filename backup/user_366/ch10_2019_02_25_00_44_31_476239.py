def libras_para_kg(kg):
    libras = 220462/100000*kg
    return libras
a = 100000
b = libras_para_kg(a);
print(b);