def separa_trios(a):
    listr = []
    for i in range(0,len(a),3):
        if i + 2 < len(a):
            trio = [a[i], a[i+1], a[i+2]]
            listr.append(trio)
        elif i + 1 < len(a):
            dupla = [a[i], a[i+1]]
            listr.append(dupla)
        else:
            listr.append([a[i]])
    return listr