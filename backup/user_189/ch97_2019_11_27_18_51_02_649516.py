dic = {
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}
def total_do_semestre_por_bairro(dic):
    d = []
    bairro = []
    total_semestral = []

    for nome in dic.keys():
        bairro.append(nome)

    for a in dic.values():
        for k in range(6):
            d.append(a[k])
    i = 0
    while i < len(d)-1:
        total = d[i] + d[i+1] + d[i+2] + d[i+3] + d[i+4] + d[i+5]
        total_semestral.append(total)
        i+=6
    
    for i in range(len(bairro)):
        print("o gasto do {0} foi de {1}".format(bairro[i],total_semestral[i]))

print(total_do_semestre_por_bairro(dic))
