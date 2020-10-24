def  total_do_semestre_por_bairro(dic):
    for k in dic.keys():
        for v in dic.values():
            Soma6=0 
            Valores=v
            for i in range(6):
                Soma6+=Valores[-i]
        dicF={k:Soma6}
        return(dicF)