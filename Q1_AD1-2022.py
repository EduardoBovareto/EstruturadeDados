v1 = [1, 3, 5, 15, 6]
v2 = [6, 3, 9, 15, 34]

#Programa Principal
v3 = []
j = 0
while j != -1:
    if v1[j] not in v2:
        v3.append(v1[j])

    if v2[j] not in v1:
        v3.append(v2[j])
    
    j += 1
    if j == len(v1):
        j = -1
''' A complexidade desse código é O(log n) pois temos uma estrutura While no código o que leva o algorítimo a demorar um certo tempo devido a análise de cada elemento da lista, mas, não tanto assim, os ifs também contribuem para o código demorar um pouco no pior caso, pois percorreremos o array duas vezes em cada if o que nos leva a uma duplicata de análises.

Complexidade Final: O(log(n))
'''