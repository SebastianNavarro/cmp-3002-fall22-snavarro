def sum(n):
    suma=0
    operaciones=0
    for n in range (1,n+1):
        suma=suma+n
        operaciones=operaciones+1
    print(operaciones)
    return suma

print(sum(5))
