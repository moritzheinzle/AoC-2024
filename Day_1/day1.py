

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

def sort_arrays(array1, array2):
    combined = list(zip(array1, array2))
    combined.sort(key=lambda x: x[0]) 
    sorted_array1, sorted_array2 = zip(*combined)
    
    return list(sorted_array1), list(sorted_array2)

def distance(array1, array2):
    sum = 0
    for i in range(len(array1)):
        sum += (array1[i] - array2[i])
    return sum


array1, array2 = input("C:\\Users\\morit_raojgbh\\AoC-2024\\Day_1\\input_day1.txt")
print(distance(array1, array2))