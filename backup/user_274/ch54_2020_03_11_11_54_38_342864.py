    if n==1:
        return [1]
    list = [1,1]
    i=1
    while i < n:
        f= list[i-1] + list[i]
        list.append(f)
        i=i+1
    return list