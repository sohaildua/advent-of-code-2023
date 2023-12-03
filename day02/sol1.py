def gamefunctions(str):  
        valSplit = str.split(':')
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
        return dictgame           
                
    
                
with open('day02/input.txt', 'r') as f:
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    dictgame = {}
    for x in data:
        dictgame = gamefunctions(x)
    
print(dictgame)

