def conta_nome(L):
    X = None
    R = R2 = []
    for cand in L:
        if cand == 'X':           
            R.append(True)

        if cand == 'Y':
            R2.append(False)

        if cand == 'B':
            pass

        if cand == 'N':
            pass

    if len(R) > len(R2):
        return f'{R} é o ganhador!'
    if len(R) == len(R2):
        return f'Nem {R} nem {R2} ganharam!'

    else:
        return f'{R2} é o ganhador!'
'''
    Mesmo com tantos ifs dentro do algorítimo, vemos que no pior caso, os ifs sempre acompanham de forma constante o for e isso nos leva a ver que só o for contribui para uma notação O(n) e que não é demorado e nem leva muito custo computacional aqui dentro. Logo, ele no pior dos casos chega longe de ser um O(n^2), bem longe, pois não há a repetição de laços, sendo assim uma notação boa e boa complexidade.
'''