def simplifica_dict(d):
    list1=[]
    list2=[]
    list3=[]
    for c, v in d.items():
        if c not in list1:
            list1.append(c)
        if v not in list2 and v not in list1:
            list2.append(v)
        list3=list1+list2
    return list3