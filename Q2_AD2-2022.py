vet = []
def Selection_Sort(v): # Trabalha de forma posicional, encontra a posição de um elemento menor de todos
    n = len(v)
    for j in range(n -1): # Percorre cada elemento
        menor = j # Pega cada indice da posição em questao
        for i in range(j, n): # É forçado a analisar cada elemento de uma vez
            if v[i] < v[menor]: # Compara pra ver se a posição anterior que é menor, é menor que a atual 
                menor = i # Se for menor ele pega essa posicao para trocar os numeros
        if v[j] > v[menor]:
            temp = v[menor]
            v[j] = v[i]
            v[i] = temp
'''
a) Como temos um for dentro do outro, temos O(n^2) para a notação, só que um dos laços, o de dentro, tem a presença de ser n-1, um a menos de tamanho do que o de fora, o que se caracteriza n(n-1)/2 para essa notação, pois se caracterizaria como um pouco menos da metade de O(n^2) dentro da notação, o que nos levaria a dizer que é um algorítimo lento.
R: (n^2 - 1)/ 2 = O(n^2)/2 iguinorando as constantes.
'''