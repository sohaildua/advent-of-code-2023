def gamefunctions(str):  
    valSplit = str.split(':')
    gameresult = 0
    listngame = []
    gameNumber = int(valSplit[0].split(' ')[1].strip())
    valBallSplit = valSplit[1].split(';')
   
    for x in valBallSplit:
        blue =0
        red = 0
        green = 0
        for data in x.split(','):
            if 'blue' in data:
                blue = int(data.strip().split(" ")[0])
            if 'green' in data:
                green = int(data.strip().split(" ")[0])
            if 'red' in data:
                red = int(data.strip().split(" ")[0])
   
        print(red, blue, green)        
                
str = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
print(gamefunctions(str))