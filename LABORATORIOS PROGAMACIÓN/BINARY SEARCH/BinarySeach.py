def binary_search(lista, low, high, target: int):
    if high >= low:
        mid = (high + low ) // 2 
        if target == lista[mid]:
            return mid
        elif lista[mid] > target:
            return binary_search(lista, low, mid-1, target)
        else:
            return binary_search(lista, mid+1, high, target)
    else:
        return -1

lista = [5, 9, 21, 32, 53, 62]
print(binary_search(lista, 0, len(lista)-1, 2))