
def gameFunctionMax(str):  
    valSplit = str.split(':')
    gameresult = 0
    listngame = []
    gameNumber = int(valSplit[0].split(' ')[1].strip())
    valBallSplit = valSplit[1].split(';')
   
    blue_max =0
    red_max = 0
    green_max = 0
    for x in valBallSplit:
        blue =0
        red = 0
        green = 0
        
        for data in x.split(','):
            if 'blue' in data:
                blue = int(data.strip().split(" ")[0])
                if blue > blue_max: 
                    blue_max = blue
            if 'green' in data:
                green = int(data.strip().split(" ")[0])
                if green > green_max: 
                    green_max = green
            if 'red' in data:
                red = int(data.strip().split(" ")[0])
                if red > red_max: 
                    red_max = red
    print("mul")
    return red_max * blue_max * green_max              
    
                
with open('day02/input.txt', 'r') as f:
    result = 0
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    dictgame = {}
    for x in data:
       result += gameFunctionMax(x)
    
    print(result)

