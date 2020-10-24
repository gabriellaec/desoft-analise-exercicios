dic={"Charles": 10, "rica": 4,} 
def calcula_tempo(dic):
    dic1={}
    for k, v in dic.items():
        t=(200/v)**(1/2)
        dic1[k]=t
		
            
    return dic1