def hora_certa(hora1,hora2):
    hora1_list=[]
    hora2_list=[]

    for h1 in hora1:
        hora1_list.append(h1)

    for h2 in hora2:
        hora2_list.append(h2)

    h01=[]
    h02=[]
    m01=[]
    m02=[]
    s01=[]
    s02=[]

    i=0
    while i<2:
        h01.append(hora1_list[i])
        h02.append(hora2_list[i])
        m01.append(hora1_list[i+3])
        m02.append(hora2_list[i+3])
        s01.append(hora1_list[i+6])
        s02.append(hora2_list[i+6])
        i+=1
    h01 = listToNumber(h01)
    h02 = listToNumber(h02)
    m01 = listToNumber(m01)
    m02 = listToNumber(m02)
    s01 = listToNumber(s01)
    s02 = listToNumber(s02)
    

    diferenca = (h02 - h01)*60**2 + (m02-m01)*60 + (s02-s01)
    
    return diferenca

def listToNumber(x):
    s = [str(i) for i in x]
    res = int("".join(s))

    return(res)

hora1="00:01:00"
hora2="00:00:00"
print(hora_certa(hora1,hora2))
