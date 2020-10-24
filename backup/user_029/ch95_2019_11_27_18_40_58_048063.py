def mais_populoso(brasil):
    soma1 = 0
    soma2 = 0
    for k,v in brasil.items():
        for t in v.values():
            if sp in v:
                soma1 += sp
            elif mg in v:
                soma2 += mg
  	if soma1 > soma2:
        return sp
    if soma2 > soma1:
        return mg
    