file = open("/workspaces/AoC_2015/day3/list.txt", "r")

positionList = []
position = [0,0]

positionList.append(position.copy())

for lines in file:
    for char in lines:
        match char:
            case ">":
                position[0] += 1
            case "<":
                position[0] -= 1
            case "^":
                position[1] += 1
            case "v":
                position[1] -= 1
            
        if not position in positionList:
            positionList.append(position.copy())

print(len(positionList))