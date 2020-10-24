sequenc=[1]
i=0
dicio={1:1}
contador=1
while ((sequenc[i]-1)/3)<1001 or sequenc[i]*2<1001:
    if ((sequenc[i]-1)/3) == int((sequenc[i]-1)/3) and ((sequenc[i]-1)/3)%2!=0:
        contador+=1
        sequenc.append(((sequenc[i]-1)/3))
        dicio[((sequenc[i]-1)/3)]=contador
        i+=1
    elif (sequenc[i]*2)%2==0:
        sequenc.append(sequenc[i]*2)
        contador+=1
        dicio[sequenc[i]*2]=contador
        i+=1
print(max(dicio,key=dicio.get))