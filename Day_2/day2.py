def input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            data.append(numbers)
    return data


def check_direction(array):
    dir = (array[0] - array[1]) > 0
    if dir:
        for i in range(len(array)-2):
            if (array[1+i] - array[2+i]) < 0:
                return False
        return True
    else:
        for i in range(len(array)-2):
            if (array[1+i] - array[2+i]) > 0:
                return False
        return True


def check_difference(array):
    for i in range(len(array)-1):
        if not 0 < abs(array[i] - array[1+i]) < 4:
            return False
        
    return True

def check_1_missing(array):
    sum = 0
    if check_direction(array) and check_difference(array):
        return True
    else:
        for j in range(len(array)):
            perm = array.pop(j)
            if check_direction(array) and check_difference(array):
                return True
            else: array.insert(j, perm)
    return False



def check_save(array):
    sum = 0
    for i in range(len(array)):
        if check_1_missing(array[i]):
            sum += 1
    return sum

print(check_save(input("C:\\Users\\mo\\Code\\AoC-2024\\Day_2\\input_day2.txt")))
