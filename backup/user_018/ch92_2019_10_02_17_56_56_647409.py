ln = []
i=0
def simplifica_dict(d):
    for k,v in d.items():
        if k[i] != v[i] or k[i]!=k[i+1] or v[i]!=v[i+1]:
            ln.append(i)
    return ln