def embaralha(L1):
    L2 = []
    i = 0
    j = len(L1) - 1
    while i != len(L1):
        temp = L1[j]
        L1[j] = L1[i]
        L1[i] = temp
        i += 1
        j -= 1
        if i == j:
            break
    L2 = L1
    return L2
vetor = [1, 2, 3, 5, 6, 8, 10, 34, 56] #Favor definir seu n de elementos para teste
print(f'O vetor inicial: {vetor}, agora invertido é:{embaralha(vetor)}')
'''
A complexidade desse algorítimo nem chega a ser grande, mesmo tendo um if que só é executado no pior caso uma unica vez, logo, se considera O(n) a notação, pois temos um laço que analisa cada elemento e que nos da um atraso no tempo de processamento e com bastantes operações, mas em tese, a notação é essa devido a simplicidade de trocas de código que ocorrem.
'''