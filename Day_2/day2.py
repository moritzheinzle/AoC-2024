def input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            data.append(numbers)
    return data

def check_safe(array):
    sum = 0
    
    for i in range(len(array)):
        
        streak = 0
        if (array[i][0] - array[i][1]) > 0: 
            
            for j in range(len(array[i])-1):
                if ((array[i][j] - array[i][j+1]) > 0) and ((array[i][j] - array[i][j+1]) < 4):
                    streak += 1 
                    
                else:
                    
                    streak = 0
    
            
        else:
            
            for j in range(len(array[i])-1):

                if ((array[i][j] - array[i][j+1]) > -4) and ((array[i][j] - array[i][j+1]) < 0):
                    streak += 1
                    
                else:
                    
                    streak = 0
            
        if streak == len(array[i])-1:
            sum += 1 
             
            streak = 0 

    return sum

        
            
        
        
                


print(check_safe(input("C:\\Users\\morit_raojgbh\\AoC-2024\\Day_2\\input_day2.txt")))