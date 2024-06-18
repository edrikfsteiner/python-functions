def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        marker = arr[i]
        j = i - 1

        while j >= 0 and marker < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = marker
    
    return arr

def merge_sort(arr):
    print(f'Chamada com {arr}')
    if len(arr) > 1:
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]

        print(f'Dividindo em {left} e {right}')

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            print(f'Posição {k} do ordenado: Comparando posição {i} de {left} com {j} de {right}')

            if left[i] < right[j]:
                print(f'Posição {i} da esquerda colocado na posição {k} do ordenado')
                arr[k] = left[i]
                i += 1
                print(f'Array ordenado: {arr}')
            else:
                print(f'Posição {j} da direita colocado na posição {k} do ordenado')
                arr[k] = right[j]
                j += 1
                print(f'Array ordenado: {arr}')
            
            k += 1
            print(f'Deslocando-se para posição {k} do ordenado')

        while i < len(left):
            print(f'Posição {i} da esquerda colocado na posição {k} do ordenado')
            arr[k] = left[i]
            i += 1
            k += 1
            print(f'{arr} ordenados')

        while j < len(right):
            print(f'Posição {j} da direita colocado na posição {k} do ordenado')
            arr[k] = right[j]
            j += 1
            k += 1
            print(f'{arr} ordenados')

    return arr

######QUICK SORT - PART 1######
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

######QUICK SORT - PART 2######
def quick_sort(vector, start, end):
    if start < end:
        position = partition(vector, start, end)

        quick_sort(vector, start, position - 1)
        quick_sort(vector, position + 1, end)

    return vector