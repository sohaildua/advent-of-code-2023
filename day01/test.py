numberMap = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
import re

def strToNumberConverter(strVal: str) -> str:
    to_array = [char for char in strVal]
    result = ''
    for char in to_array:
        result += char
        for key, value in numberMap.items():
            result = result.replace(key, str(numberMap[key]))
    return result
strval = "xlleightwo72tctrvxfk4one"
print(strToNumberConverter(strval))
