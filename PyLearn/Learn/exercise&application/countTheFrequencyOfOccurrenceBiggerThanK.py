# def countFrequency(nums, k):
#     frequen = {}
#     for num in nums:
#         if num in frequen:
#             frequen[num] += 1
#         else:
#             frequen[num] = 1
#     result = [num for num, count in frequen.items() if count > k]
#     result.sort()
#     return result
from collections import Counter

def countFrequency(nums, k):
    frequen = Counter(nums) # Sử dụng Counter để đếm tần suất của từng phần tử
    result = [num for num, count in frequen.items() if count > k]  # Lọc các phần tử có tần suất lớn hơn k và sắp xếp theo thứ tự tăng dần
    result.sort() # Sắp xếp theo thứ tự tăng dần
    return result

nums = list(map(int, input().split()))
k = int(input())
print(countFrequency(nums, k))



