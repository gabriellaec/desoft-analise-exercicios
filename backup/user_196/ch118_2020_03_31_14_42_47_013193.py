def reflexao_total_interna(n1, n2, ang2):
    math.sin(ang1) = (n2* math.sin(ang2)) / n1
    if math.sin(ang1) > 1:
        return True
    else:
        return False
    