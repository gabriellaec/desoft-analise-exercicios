i=0
while i<len(l):
    if ((l[i]+l[i+2])/2)==l[i+1]:
        return "PA"
    elif (l[i+2]/l[i+1])==(l[i+1]/l[i]):
        return "PG"
    elif (l[0]+l[i+2])/2==l[i+1] and (l[i+2]/l[i+1])==(l[i+1]/l[i]):
        return "AG"
    else:
        return "NA"
    i+=1