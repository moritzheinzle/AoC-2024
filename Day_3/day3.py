def read_file_to_string(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = "C:\\Users\\mo\\Code\\AoC-2024\\Day_3\\input_day3.txt"
file_content = read_file_to_string(file_path)



def find_mul(s, idx):
    substring = "mul("
    for i in range(4):
        if not s[idx+i] == substring[i]:
            return False
    return True



def find_number_at_index(s, i):
    for length in range(1, 4):
        substring = s[i:i+length] 
        if substring.isdigit(): 
            if i + length >= len(s) or not s[i+length].isdigit():
                return int(substring), length
    return False

def check_do_dont(s, idx):
    if idx + 4 <= len(s):
        substring = "do()"
        if all(s[idx+i] == substring[i] for i in range(4)):
            return 2
    if idx + 7 <= len(s):
        substring = "don't()"
        if all(s[idx+i] == substring[i] for i in range(7)):
            return 3

    return False



def check_memory(s, i):
    if find_mul(s, i):

        if find_number_at_index(s, i+4):
            number = []
            number.append(list(find_number_at_index(s, i+4)))
            if s[i+4+number[0][1]] == ",":
                if find_number_at_index(s,i+5+number[0][1]):
                    number.append(list(find_number_at_index(s, i+5+number[0][1])))
                    if s[i+5+number[0][1]+number[1][1]] == ")":
                        return number
                    
def solve_memory(s):
    product = 0
    flag = 0
    for i in range(len(s)):
        
        res = check_do_dont(s, i)
        if res == 2:
            flag = 0
        if res == 3:
            flag = 1
        if flag == 0:
            if check_memory(s, i):
                res = check_memory(s, i)
                product += (res[0][0]* res[1][0])
    return product
    
print(solve_memory(file_content))