

def input(filename):
    array1 = []
    array2 = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                array1.append(int(parts[0]))
                array2.append(int(parts[1]))
    return array1, array2

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quicksort(left) + middle + quicksort(right)  
import bisect

import bisect

def count_occurrences(arr, target):
    left_index = bisect.bisect_left(arr, target)
    if left_index < len(arr) and arr[left_index] == target:
        right_index = bisect.bisect_right(arr, target)
        return right_index - left_index
    else:
        return 0

def distance(array1, array2):
    sum = 0
    for i in range(len(array1)):
        if array1[i] < array2[i]:
            sum += array2[i] - array1[i]
        else:
            sum += array1[i] -array2[i]  
              
            
    return sum

def difference(array1, array2):
    sum = 0
    for i in range(len(array1)):
        sum += (array1[i] * count_occurrences(array2, array1[i]))

    return sum
array1, array2 = input("C:\\Users\\morit_raojgbh\\AoC-2024\\Day_1\\input_day1.txt")

print(distance(quicksort(array1), quicksort(array2)))
print(difference(quicksort(array1), quicksort(array2)))