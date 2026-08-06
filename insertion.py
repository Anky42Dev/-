arr = [5,2,5,3,1,4]
def division(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = division(arr[:mid])
    right = division(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result = []
    i=j=0
    while len(left)>i and len(right)>j:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(division(arr))
    