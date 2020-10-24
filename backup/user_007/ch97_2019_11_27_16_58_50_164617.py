def total_do_semestre_por_bairro(dic):
    ans = {}
    for i in dic:
        ans[i] = sum(dic[i][6:])
    return ans