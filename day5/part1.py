
def  main():
    nice = 0
    file = open("list.txt", "r")

    for lines in file:
        if rule_1(lines) and rule_2(lines) and rule_3(lines):
            nice += 1
    print(nice)

def rule_1(lines):
    vCount = 0
    for letters in lines:
        if letters in "aeiou":
            vCount += 1

    if vCount >= 3:
        return True
    else:
        return False

def rule_2(lines):
    for i in range(len(lines)):
        try:
            if lines[i] == lines[i + 1]:
                return True
        except IndexError:
            pass
    return False


def rule_3(lines):
    if "ab" in lines or "cd" in lines or "pq" in lines or "xy" in lines:
        return False
        
    return True


main()
