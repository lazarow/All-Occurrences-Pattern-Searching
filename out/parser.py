import re

def parse_real_time(time_str):
    match = re.search(r'real\s+(\d+)m([\d,]+)s', time_str)
    if match:
        minutes = int(match.group(1))
        seconds = float(match.group(2).replace(',', '.'))
        total_seconds = minutes * 60 + seconds
        return str(total_seconds).replace('.', ',') if total_seconds <= 300 else "timeout"
    return None

def parse_log_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    results = []
    dataset_name = None
    first_count = None
    first_real_time = None
    second_count = None
    second_real_time = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("====="):
            if dataset_name and first_count is not None and first_real_time is not None:
                results.append((dataset_name, first_count, first_real_time, second_count, second_real_time))
            
            dataset_name = line.strip("= ")
            first_count = None
            first_real_time = None
            second_count = None
            second_real_time = None
            continue
        
        if re.fullmatch(r'\d+', line) and first_count is None:
            first_count = int(line)
            continue
        
        if line.startswith("real") and first_real_time is None:
            first_real_time = parse_real_time(line)
            continue
        
        if re.fullmatch(r'\d+', line) and first_count is not None and second_count is None:
            second_count = int(line)
            continue
        
        if line.startswith("real") and first_real_time is not None and second_real_time is None:
            second_real_time = parse_real_time(line)
    
    if dataset_name and first_count is not None and first_real_time is not None:
        results.append((dataset_name, first_count, first_real_time, second_count, second_real_time))
    
    return results

log_file = "results.11022025.log"
extracted_data = parse_log_file(log_file)

for data in extracted_data:
    print(data[1])