import re
with open('input.txt', 'r') as f:
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    
    print(data)
    result = 0
    for value in data:
        tens_number =re.search(r'[\d]{1}', value).group()
        digit_number = re.search(r'[\d]{1}', value[::-1]).group()
        e
        total_digit_number = int(tens_number + digit_number) 
        result += total_digit_number
    print(result)
        
