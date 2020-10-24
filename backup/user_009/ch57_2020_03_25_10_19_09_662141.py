def ehpa(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not(l[index + 1] - l[index] == delta):
            return 'n'
    return 'PA'

def is_geometric(l):
    if len(l) <= 1:
        return 'PG'
    # Calculate ratio
    ratio = l[1]/float(l[0])
    # Check the ratio of the remaining
    for i in range(1, len(l)):
        if l[i]/float(l[i-1]) != ratio: 
            return 'n'
    return 'PG' 

def verifica_progressao(l):
    if len(l) <=1:
        return 'NA'
    
    pg = is_geometric(l)
    pa = ehpa(l)

    if pa == 'PA' and pg == 'PG':
        return 'AG'
    elif pa == 'PA':
        return 'PA'
    elif pg == 'PG':
        return 'PG'
    else:
        return 'NA'