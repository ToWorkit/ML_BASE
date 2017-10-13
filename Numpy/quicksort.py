# 快速排序
# 待补充
# 不对
def quicksort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  print(len(arr) // 2)
  print(pivot)
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quicksort(left) + quicksort(middle) + quicksort(right)
print(quicksort([3, 6, 8, 2, 10, 1]))  

