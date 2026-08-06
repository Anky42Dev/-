arr= [2,5,33,67,90]
def radix_sort(arr):
    max_num = max(arr)
    place = 1
    while max_num // place > 0 :
        buckets = [[] for _ in range(10)]
        for num in arr:
            digits = (num // place % 10)
            buckets[digits].append(num)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        place *= 10
    return arr
print(radix_sort(arr))
    


