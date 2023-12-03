numberMap = {'zero':0,'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
sorted_keys = sorted(numberMap.keys(), key=len, reverse=True)
import re
def strToNumberConverter(strVal: str) -> str:
    to_array = [char for char in strVal]
    result = ''
    for char in to_array:
        result += char
        for key, value in numberMap.items():
            result = result.replace(key, str(numberMap[key]))
    return result
with open('input.txt', 'r') as f:
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    
    
    result = 0
    for value in data:
        strVal = strToNumberConverter(value)
        print(strVal)
        tens_number =re.search(r'[\d]{1}', strVal).group()
        digit_number = re.search(r'[\d]{1}', strVal[::-1]).group()
        
        total_digit_number = int(tens_number + digit_number) 
        #print(total_digit_number)
        result += total_digit_number
    print(result)

