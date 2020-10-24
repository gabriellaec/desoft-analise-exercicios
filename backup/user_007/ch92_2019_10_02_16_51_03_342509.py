def simplifica_dict(d):
    ans = []
    for i in d:
        if i not in ans:
            ans.append(i)
        if d[i] not in ans:
            ans.append(d[i])
    return ans