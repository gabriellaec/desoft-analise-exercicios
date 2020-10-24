def total_do_semestre_por_bairro(dic):
    total=list(dic.values())
    i=6
    while i<12:
    	total.remove(i)
    nomes=list(dic.keys())
    final={"nomes[0]":total[0],
           "nomes[1]":total[1],
           "nomes[2]":total[2],
           "nomes[3]":total[3],
           "nomes[4]":total[4],
           "nomes[5]":total[5]
          }
    return final