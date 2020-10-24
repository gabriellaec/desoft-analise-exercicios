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
        total=0
    return final        
            
def bairro_mais_custoso(dicio):
    maior=0
    totais=total_do_semestre_por_bairro(dicio)
    for i in totais:
        totalbairro=totais[i]
        if totalbairro>maior:
            maior=totalbairro
            bairro=i
    return bairro
        