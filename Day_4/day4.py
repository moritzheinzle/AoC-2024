def input_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
        file_content = [list(line) for line in content.splitlines()]
        return file_content
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

file_path = "C:\\Users\\mo\\Code\\AoC-2024\\Day_4\\input_day4.txt"
file_content = input_txt(file_path)



def horizontal(s):
    occ = 0
    
    substring = "XMAS"
    for i in range(len(s)):
        fwd = 0
        bwd = 0
        for j in range(len(s[i])):
            if s[i][j] == substring[fwd]:
                fwd += 1
            else:
                fwd = 0
            if s[i][j] == substring[len(substring)-1-bwd]:
                bwd += 1
            else:
                bwd = 0
            if fwd == len(substring):
                occ += 1
                fwd = 0
            if bwd == len(substring):
                occ += 1
                bwd = 0
    return occ

def vertical(s):
    occ = 0
    
    substring = "XMAS"
    for i in range(len(s[0])):
        fwd = 0
        bwd = 0
        for j in range(len(s)):
            if s[j][i] == substring[fwd]:
                fwd += 1
            else:
                fwd = 0
            if s[j][i] == substring[len(substring)-1-bwd]:
                bwd += 1
            else:
                bwd = 0
            if fwd == len(substring):
                occ += 1
                fwd = 0
            if bwd == len(substring):
                occ += 1
                bwd = 0
    return occ


           
def di