def eh_bissexto:
    if x%100==0 and x%400!=0:
        return(False)
    if x%4==0:
        return(True)
    else:
        return(False)