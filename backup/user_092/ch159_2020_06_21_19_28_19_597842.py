with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
    
    dic1 = texto.replace('{','} ')
    dic2 = dic1.replace('[',' ]')
    dic3 = dic2.replace(']','} ')
    dic4 = dic3.replace(':','} ')
    dic5 = dic4.replace(',','} ')
    dic6 = dic5.replace('"','} ')
    dic7 = dic6.replace('}',' ')
    dic = dic7.split()

    i = 4
    c = 0
    while i<len(dic):
        a = int(dic[i])
        b = float(dic[i+2])
        c += a*b
        i += 6
    print(c)