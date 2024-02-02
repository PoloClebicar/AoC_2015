def main():
    file = open("/mnt/c/Users/thepo/Documents/GitHub/AoC_2015/list.txt", "r")

    rowArray = []
    collumArray = []
    size = 1000
    answer = 0

    for _ in range(size):
        collumArray.append(0)
    
    for _ in range(size):
        rowArray.append(collumArray.copy())

    for lines in file:
        first_half, second_half = lines.split("through")
        first_half = first_half.strip()
        second_half = second_half.strip()

        try:
            trash, action, startPosition = first_half.split(" ")
        except ValueError:
            action, startPosition = first_half.split(" ")

        if action == "on":
            rowArray = turn_on(rowArray, startPosition, second_half)
        elif action == "off":
            rowArray = turn_off(rowArray, startPosition, second_half)
        elif action == "toggle":
            rowArray = toggle(rowArray, startPosition, second_half)

    for i in range(size):
        for j in range(size):
            if rowArray[i][j] == 1:
                answer += 1
    print(answer)

def turn_on(array, startPosition, endPosition):
    rowStart = int(startPosition.split(",")[0])
    collumStart = int(startPosition.split(",")[1])
    rowEnd = int(endPosition.split(",")[0])
    collumEnd = int(endPosition.split(",")[1])

    collumStartCLone = collumStart

    while rowStart <= rowEnd:
        while collumStartCLone <= collumEnd:
            array[rowStart][collumStartCLone] = 1

            collumStartCLone += 1
            
        collumStartCLone = collumStart
        rowStart += 1
    return array

def turn_off(array, startPosition, endPosition):
    rowStart = int(startPosition.split(",")[0])
    collumStart = int(startPosition.split(",")[1])
    rowEnd = int(endPosition.split(",")[0])
    collumEnd = int(endPosition.split(",")[1])

    collumStartCLone = collumStart

    while rowStart <= rowEnd:
        while collumStartCLone <= collumEnd:
            array[rowStart][collumStartCLone] = 0

            collumStartCLone += 1
            
        collumStartCLone = collumStart
        rowStart += 1
    return array

def toggle(array, startPosition, endPosition):
    rowStart = int(startPosition.split(",")[0])
    collumStart = int(startPosition.split(",")[1])
    rowEnd = int(endPosition.split(",")[0])
    collumEnd = int(endPosition.split(",")[1])

    collumStartCLone = collumStart

    while rowStart <= rowEnd:
        while collumStartCLone <= collumEnd:
            if array[rowStart][collumStartCLone] == 0:
                array[rowStart][collumStartCLone] = 1
            elif array[rowStart][collumStartCLone] == 1:
                array[rowStart][collumStartCLone] = 0              

            collumStartCLone += 1
            
        collumStartCLone = collumStart
        rowStart += 1
    return array
main()