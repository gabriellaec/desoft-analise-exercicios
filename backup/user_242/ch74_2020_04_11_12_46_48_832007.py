def conta_bigramas(string):
    dict={}
    i=0
    for i in range(len(string)-1):
        brigrama = string[i]+ string[i+1]
        if brigrama not in dict:
            dict[bigrama]=1
        else:
            dict[brigrama] +=1
    return dict