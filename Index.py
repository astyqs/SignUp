# def bubble (lst):
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 swap = True
# nums = [1, 3,45, 21, 99]

# bubble(nums)
# print(nums)

# def insertion(list_nums):
#     for i in range(1, len(list_nums)):
#         item = list_nums[i]
#         i2 = i - 1
#         while i2 >= 0 and list_nums[i2] > item:
#             list_nums[i2 + 1] = list_nums[i2]
#             i2 -= 1
#         list_nums[i2 + 1] = item
# nums = [1, 2,9889, 23,4,54,62,32,2]
# insertion(nums)
# print(nums)

# def solution(lst):
#     for i in range(len(lst)):
#         index = i  
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[index]:
#                 index = j
#         lst[i], lst[index] = lst[index], lst[i]

# nums = [3, 1, 4, 2, 21, 321, 0, 99]
# solution(nums)
# print(nums)

# target = 155
# low, high = 0, len(nums) - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if nums[mid] == target:
#         found = True
#         break
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1
# print(found)

# def heapify(sort_nums, heap_size, root):
#     l = root
#     left = (2 * root) + 1
#     right = (2 * root) + 2
#     if left < heap_size and sort_nums[left] > sort_nums[l]:
#         l = left
#     if right < heap_size and sort_nums[right] > sort_nums[l]:
#         l = right
#     if l != root:
#         sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
#         heapify(sort_nums, heap_size, l)
# def heap(sort_nums):
#     size = len(sort_nums)
#     for i in range(size, - 1, -1,):
#         heapify(sort_nums, size, i)
#     for i in range(size - 1, 0, -1):
#         sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
#         heapify(sort_nums, i, 0)
# nums = [8, 7, 44, 11, 9]
# heap(nums)
# print(nums)

# import random
# lst = []
# a = int(input("Введите число: "))
# for i in range(a):
#     lst.append(random.randint(0, 100))
# def bubble (lst):
#      swap = True
#      while swap:
#          swap = False
#          for i in range(len(lst)-1):
#              if lst[i] > lst[i+1]:
#                  lst[i], lst[i+1] = lst[i+1], lst[i]
#                  swap = True

# bubble(a)
# print(lst)

def bubble(arr):
    
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



user_array = []


print("Введите 10 чисел:")
for _ in range(10):
    num = int(input("Введите число: "))
    user_array.append(num)

print("Массив до сортировки:", user_array)


bubble(user_array)

print("Массив после сортировки:", user_array)
