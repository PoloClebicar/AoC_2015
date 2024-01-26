file = open("/workspaces/AoC_2015/day2/list.txt", "r")

ans = 0

for lines in file:
    l,w, h = lines.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    if l >= w and l >= h:
        sideOne = w
        sideTwo = h
    if w >= l and w >= h: 
        sideOne = l
        sideTwo = h
    if h >= l and h >= w:
        sideOne = l
        sideTwo = w

    ans += 2*sideOne + 2*sideTwo + (w*l*h) 

print(ans)