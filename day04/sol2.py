from collections  import defaultdict

with open('day04/input.txt', 'r') as f:
    lines = f.readlines()
    data = [entry.strip() for entry in lines]
    common = 0
    N = defaultdict(int)
    for i,line in enumerate(lines):
        N[i]+=1
        lineNumber = line.split(':')[1].split('|');
        print(lineNumber)
        first = lineNumber[0].strip()
        win = lineNumber[1].strip()
        listfirst = []
        winfirst = []
        for entry in first.split(' '):
            print(entry)
            if entry.isdigit():
                listfirst.append(int(entry))
        for entry in win.split(' '):
            if entry.isdigit():
                winfirst.append(int(entry))
        set1 = set(listfirst)
        set2 = set(winfirst)
        common_elements = set1.intersection(set2)        
        print("Common Elements:", common_elements)
        print("Number of Common Elements:", len(common_elements))
        if len(common_elements) >0:
            common += 2**(len(common_elements)-1)
        for j in range(len(common_elements)):
            N[i+1+j] += N[i] 
        print(common)
        print(sum(N.values()))    
        
            