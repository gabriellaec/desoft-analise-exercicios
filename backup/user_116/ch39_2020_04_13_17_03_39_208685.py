sequenc=[1]
i=0
while ((sequenc[i]-1)/3)<1000 or sequenc[i]*2<1000:
    if ((sequenc[i]-1)/3) == int((sequenc[i]-1)/3) and ((sequenc[i]-1)/3)%2!=0:
        sequenc.append(((sequenc[i]-1)/3))
        i+=1
    elif (sequenc[i]*2)%2==0:
        sequenc.append(sequenc[i]*2)
        i+=1
print(sequenc[-1])
