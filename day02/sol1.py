
def gamefunctions(str):  
        count = 0
        valSplit = str.split(':')
        gameNumber = int(valSplit[0].split(' ')[1].strip())
        valBallSplit = valSplit[1].split(';')
        for x in valBallSplit:
            blue =0
            red = 0
            green = 0
            for data in x.split(','):
                print(len(x.split(',')))
                if 'blue' in data:
                    blue = int(data.strip().split(" ")[0])
                if 'green' in data:
                    green = int(data.strip().split(" ")[0])
                if 'red' in data:
                    red = int(data.strip().split(" ")[0])
            if blue<=14 and green<=13 and red<=12:
                count = count + 1
                if count == len(valBallSplit):
                    return gameNumber
            
        return 0                
    
                
with open('day02/input.txt', 'r') as f:
    result = 0
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    dictgame = {}
    for x in data:
       result += gamefunctions(x)
    
    print(result)

