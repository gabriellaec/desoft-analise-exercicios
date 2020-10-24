def mais_populoso(br):
    mais_pop = ''
    pop = 0
    for estado in br:
        for cidade in br[estado]:
            if br[estado][cidade] > pop:
                pop = br[estado][cidade]
                mais_pop = cidade

    return mais_pop