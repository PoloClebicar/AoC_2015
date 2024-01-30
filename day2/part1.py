file = open("list.txt", "r")

ans = 0

for lines in file:
    l,w, h = lines.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    sideOne = 2*l*w
    sideTwo = 2*w*h
    sideThree = 2*h*l

    smallSide = sideOne
    
    if sideTwo < smallSide:
        smallSide = sideTwo

    if sideThree < smallSide:
        smallSide = sideThree

    ans += sideOne + sideTwo + sideThree + smallSide/2

print(ans)