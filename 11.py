# Задание 2 — измерь скорость сам 
# Напиши скрипт, который создаёт отсортированный список numbers = list(range(N)) 
# и сравнивает время linear_search и binary_search для худшего случая (target = N - 1), используя time.perf_counter().
# Запусти скрипт трижды — для N = 1 000, N = 10 000 и N = 1 000 000 — и занеси результаты в таблицу (N, время linear_search, время binary_search).\
#  В комментарии ответь: во сколько раз выросло время linear_search при переходе от 1 000 к 1 000 000? 
# А время binary_search? Совпадает ли это с тем, что предсказывает теория (O(n) и O(log n))?
import time
N = 1000000
numbers = list(range(N))
target = N-1
start = time.perf_counter()
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
linear_search(numbers, target)
end = time.perf_counter()
print(f'LS results: {end - start}') #(1000-2.7499976567924023e-05, 10000-0.0002611999516375363,1000000-0.030179699999280274) # время выросло в 1097 раз с 1000 на 1000000 что соответсвует сложности O(n) 
start = time.perf_counter()
def binary_search(arr,target):
    left = 0 
    right = len(arr) -1 
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            right = mid-1
        else:
            left = mid +1
    return -1
binary_search(numbers,target)
end = time.perf_counter()
print(f'BS results: {end - start}') #(1000 -1.3999990187585354e-05, 10000 - 1.0899966582655907e-05,1000000 - 2.6899971999228e-05) время выросло в 2 раза с 1000 на 1000000 что соответствует сложности O(log N)
