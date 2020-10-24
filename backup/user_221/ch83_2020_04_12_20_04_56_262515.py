l = []
c = 0
j = 0

for nom, nota in d.items():
    if l == [[]]:
        l.append([])
        l[c].append(nom[0])
        l[c].append(1)
        l[c].append(nota)
        c += 1
    else:
        k = 0
        for j in range(c):
            if nom[0] == l[j][0]:
                l[j][1] += 1
                l[j][2] = (l[j][2]*(l[j][1] - 1) + nota) / l[j][1]
                j += 1
            else:
                k += 1
                j += 1
        if k == c:
            l.append([])
            l[c].append(nom[0])
            l[c].append(1)
            l[c].append(nota)
            c += 1

nd = {}
i = 0
for i in range(c):
    nd[l[i][0]] = l[i][2]

print(nd)