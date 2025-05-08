import random

def bubble_sort(arr, stats):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            stats["comparacoes"] += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                stats["trocas"] += 1


def selection_sort(arr, stats):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            stats["comparacoes"] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            stats["trocas"] += 1


def insertion_sort(arr, stats):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            stats["comparacoes"] += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                stats["trocas"] += 1
                j -= 1
            else:
                break
        arr[j + 1] = key


def merge_sort(arr, stats):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            stats["comparacoes"] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                stats["trocas"] += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], stats)
    right = merge_sort(arr[mid:], stats)
    return merge(left, right)


def quick_sort(arr, stats):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi-1)
            _quick_sort(items, pi+1, high)

    
    def partition(items, low, high):
        # novo: escolha pivô aleatório
        pivot_idx = random.randint(low, high)
        items[pivot_idx], items[high] = items[high], items[pivot_idx]
        
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            stats["comparacoes"] += 1
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                stats["trocas"] += 1
        items[i+1], items[high] = items[high], items[i+1]
        stats["trocas"] += 1
        return i + 1

    _quick_sort(arr, 0, len(arr)-1)


def heap_sort(arr, stats):
    def heapify(n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n:
            stats["comparacoes"] += 1
            if arr[l] > arr[largest]:
                largest = l
        if r < n:
            stats["comparacoes"] += 1
            if arr[r] > arr[largest]:
                largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            stats["trocas"] += 1
            heapify(n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        stats["trocas"] += 1
        heapify(i, 0)
