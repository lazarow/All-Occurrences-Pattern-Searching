import sys

def find_smallest_largest_regex(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if len(lines) < 2:
        print("File must contain at least one regex after the first line.")
        return
    
    regexes = [line.strip() for line in lines[1:] if line.strip()]
    
    smallest = min(regexes, key=len)
    largest = max(regexes, key=len)
    
    print("Smallest regex:", len(smallest), smallest)
    print("Largest regex:", len(largest), largest)
    
    return smallest, largest

file_path = sys.argv[1]
find_smallest_largest_regex(file_path)