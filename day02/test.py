def gamefunctions(str):  
    str = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    valSplit = str.split(':')
    dictgame = {}
    listngame = []
    gameNumber = int(valSplit[0].split(' ')[1].strip())
    valBallSplit = valSplit[1].split(';')
    blue = 0
    red = 0
    green = 0 
    for x in valBallSplit:
        for data in x.split(','):
            if 'blue' in data:
                blue += int(data.strip().split(" ")[0])
            if 'green' in data:
                green += int(data.strip().split(" ")[0])
            if 'red' in data:
                red += int(data.strip().split(" ")[0])
    listngame.append({"blue": blue})
    listngame.append({"green": green})
    listngame.append({"red": red})
    dictgame[gameNumber] = listngame
    print(dictgame)
    return dictgame           
                
    
                