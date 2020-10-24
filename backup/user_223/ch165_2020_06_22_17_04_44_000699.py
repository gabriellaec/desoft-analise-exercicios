def mais_populoso(dicio):
    mais_pop = 0
    for d in dicio_values():
        for v in d_values():
            for hab in v_keys():
                pop = sum(hab)
                if pop > mais_pop:
                    mais_pop = pop
    return mais_pop