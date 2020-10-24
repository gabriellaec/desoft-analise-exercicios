def junta_nomes (listn1,listn2,lists):
    listf=[]
    for i in range (len(lists)):
        for n in range (len(listn1)):
            listf.append(listn1[n]+' '+lists[i])
        for m in range (len(listn2)):
            listf.append(listn2[m]+' '+lists[i])
    return listf
