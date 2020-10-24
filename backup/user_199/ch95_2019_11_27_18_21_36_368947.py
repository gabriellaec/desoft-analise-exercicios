dicionario={'sp': {'sp1':600,'camp':100},
            'mg': {'bh':500,'uber':10}}

def mais_populoso(dicionario):
    s1=0
    s2=0
    for k,v in dicionario.items():
       
        for valores in v.values(): 
            if 'sp1' in v:
                s1+=valores
            elif 'bh' in v:
                s2+=valores
    if s1>s2:
        return 'sp'
    elif s2>s1:
        return 'mg'
 
print(mais_populoso(dicionario))