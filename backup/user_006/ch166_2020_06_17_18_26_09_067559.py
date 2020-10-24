def total_do_semestre_por_bairro(dicio):
    final={}
    total=0
    for i in dicio:
        lista=dicio[i]
        e=6
        while e<12:
            total=total+lista[e]
            e=e+1
        final[i]=total
    return final        
            
    