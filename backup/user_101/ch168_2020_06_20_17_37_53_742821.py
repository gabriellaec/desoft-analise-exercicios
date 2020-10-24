def login_disponivel(log, l):
    if log not in l:
        return log
    else:
        log = log +'1'
        return log