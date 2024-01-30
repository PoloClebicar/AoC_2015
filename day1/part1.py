file = open("list.txt", "r")

ans = 0

for line in file:
    for char in line:
        if char == "(":
            ans += 1
        elif char == ")":
            ans -= 1

print(ans)