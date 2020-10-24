def mais_populoso(dicio):
    mais_pop = 0
    for d in dicio_values():
        for v in d_values():
            for k in v_keys():
                pop = sum(k)
                if pop > mais_pop:
                    mais_pop = pop
    return mais_pop