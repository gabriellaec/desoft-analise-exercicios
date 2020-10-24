def calcula_tempo(atletas):
    v={}
    for e in atletas:
        x=atletas[e]
        v[e]=(200/x)**0.5
    return v
atletas={'a': 8, 'b':10,'c':15}
print(calcula_tempo(atletas))
