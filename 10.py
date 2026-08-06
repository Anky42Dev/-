# Задание 1 — напиши оба поиска сам 
# Не подглядывая в материал, напиши функции linear_search(arr, target) и binary_search(arr, target) самостоятельно. 
# Проверь их на списке arr = [2, 5, 9, 14, 20, 27, 35, 48, 60, 77]: 
# — найди индекс числа 48 обоими способами; 
# — убедись, что для числа 100 (которого нет в списке) обе функции возвращают -1. 
# Дополнительно: специально переставь пару чисел в списке местами, чтобы он перестал быть отсортированным,cd
# и запусти binary_search для числа, которое точно есть в списке. Опиши в комментарии, что произошло и почему. 
arr = [2,5,9,14,20,27,35,48,60,77]
target = 48
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search(arr,target))
arr = [2,5,9,14,20,27,35,48,60,77]
target = 48
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
print(binary_search(arr,target)) 
#В терминале выводится -1 так как код не видит наш target а именно 48 , 
# так как мы поменяли 9 и 48 местами. При сортировке 48 должен быть справа 
#  но так как мы специально написали слева он не видит ее из-за чего считает что ее нет в списке и выводит -1



        

