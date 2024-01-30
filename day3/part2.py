file = open("list.txt", "r")

positionList = []
positionA = [0,0]
positionB = [0,0]
realSanta = True


positionList.append([0,0])

for lines in file:
    for char in lines:
        match char:
            case ">":
                if realSanta:
                    positionA[0] += 1
                    realSanta = False
                else:
                    positionB[0] += 1
                    realSanta = True
            case "<":
                if realSanta:
                    positionA[0] -= 1
                    realSanta = False
                else:
                    positionB[0] -= 1
                    realSanta = True
            case "^":
                if realSanta:
                    positionA[1] += 1
                    realSanta = False
                else:
                    positionB[1] += 1
                    realSanta = True
            case "v":
                if realSanta:
                    positionA[1] -= 1
                    realSanta = False
                else:
                    positionB[1] -= 1
                    realSanta = True
            
        if not positionA in positionList:
            positionList.append(positionA.copy())
        
        if not positionB in positionList:
            positionList.append(positionB.copy())

        
print(len(positionList))