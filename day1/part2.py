file = open("/workspaces/AoC_2015/day1/list.txt", "r")

ans = 0
ans2 = 0

for line in file:
    for char in line:
        if char == "(":
            ans += 1
        elif char == ")":
            ans -= 1
        
        ans2 += 1
        if ans == -1:
            print(ans2)
            break


#print(ans)