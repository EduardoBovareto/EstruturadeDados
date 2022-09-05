def fat(v):
    if v == 1:
        return 1
    return v * fat( v - 1)
    

fat(6)
# temp = 1
# n = int(input('number: '))
# for i in range(1, n + 1):
#     temp = temp * i
# print(temp)