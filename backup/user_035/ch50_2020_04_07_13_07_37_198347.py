def junta_nome_sobrenome(ln, ls):
    i = 0
    espaço =[] 
    while i<=len(ln)-1:
        nome_completo = ln[i] + espaço + ls[i]
        i += 1
    return nome_completo