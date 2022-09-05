temp = 1
n = int(input('write number'))
for i in range(1, n):
    temp += i * temp # fatorial de trás para frente, de forma que se some as multiplicações.
    pass
print(temp)
