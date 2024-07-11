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

############ QUICK SORT - PART 1 ############
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

############ QUICK SORT - PART 2 ############
def quick_sort(arr, start, end):
    if start < end:
        position = partition(arr, start, end)

        quick_sort(arr, start, position - 1)
        quick_sort(arr, position + 1, end)

    return arr

# The merge sort below has prints that helps explain how it's working,
# as I've found it the most difficult to have a grasp on, and the prints
# really helped me to get a understanding on it, while it's running.

def merge_sort(arr):
    print(f'Calling {arr}')
    if len(arr) > 1:
        half = len(arr)//2
        left = arr[:half]
        right = arr[half:]

        print(f'Dividing in {left} and {right}')

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            print(f'Position {k} of the sorted array: Comparing position {i} from {left} with {j} from {right}')

            if left[i] < right[j]:
                print(f'Position {i} from left put in position {k} of the sorted array')
                arr[k] = left[i]
                i += 1
                print(f'Sorted array: {arr}')
            else:
                print(f'Position {j} from right put in position {k} of the sorted array')
                arr[k] = right[j]
                j += 1
                print(f'Sorted array: {arr}')
            
            k += 1
            print(f'Changing to position {k} of the sorted array')

        while i < len(left):
            print(f'Position {i} from left put in position {k} of the sorted array')
            arr[k] = left[i]
            i += 1
            k += 1
            print(f'{arr} sorted')

        while j < len(right):
            print(f'Position {j} from right put in position {k} of the sorted array')
            arr[k] = right[j]
            j += 1
            k += 1
            print(f'{arr} sorted')

    return arr

# Uncomment the code below to run the functions
'''
list = [2, 4, 1, 5, 3, 7, 9, 8, 6]
list_bubble = bubble_sort(list)
print(list_bubble)
list_insertion = insertion_sort(list)
print(list_insertion)
list_quick = quick_sort(list, 0, len(list) - 1)
print(list_quick)
list_merge = merge_sort(list)
print(list_merge)
'''