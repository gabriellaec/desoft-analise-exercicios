def bairro_mais_custoso(dic):
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
        if total_semestral[i] == max(total_semestral):
            print(" o bairro mais custoso foi: {0}".format(bairro[i]))

print(bairro_mais_custoso(dic))