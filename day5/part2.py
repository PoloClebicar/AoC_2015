def  main():
    nice = 0
    rule1 = 0
    rule2 = 0
    file = open("/media/polo/Polo-HD/GitHub/AoC_2015/list.txt", "r")

    for lines in file:
    #   if rule_1(lines):
    #       rule1 += 1
    #   if rule_2(lines):
    #       rule2 += 1

    #   print(rule1, rule2)
    
       if rule_1(lines) and rule_2(lines):
            nice += 1
    print(nice)

def rule_1(lines):
    for i in range(len(lines) - 1):
        pair_1 = lines[i] + lines[i+1]
        try:
            for j in range(len(lines)):
                pair_2 = lines[j + 2 + i] + lines[j + 3 + i]
                if pair_1 == pair_2:
                    return True
        except IndexError:
            pass

    return False



def rule_2(lines):
    for i in range(len(lines)):
        try:
            if lines[i] == lines[i + 2]:
                return True
        except IndexError:
            pass
    return False
    


main()