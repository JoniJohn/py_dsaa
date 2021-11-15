def bubbleSortAsc(arr):
    """
    A simple bubble sort in ascending order
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            # if not sorted
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSortDesc(arr):
    """
    A simple bubble sort in descending order
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            # if not sorted
            if arr[j] < arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionSortAsc(arr):
    """
    Sorts an array using Selection Sort algorithm in ascending order
    """
    flag = False
    smallest = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
                flag = True
        if flag == True:
            # swap
            arr[smallest], arr[i] = arr[i], arr[smallest]
            flag = False
        else:
            smallest = i + 1
    return arr


def selectionSortDesc(arr):
    """
    Sorts an array using Selection Sort algorithm in descending order
    """
    flag = False
    largest = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[largest] < arr[j]:
                largest = j
                flag = True
        if flag == True:
            # swap
            arr[largest], arr[i] = arr[i], arr[largest]
            flag = False
        else:
            largest = i + 1
    return arr
