def catAndMouse(x, y, z):
    xres = abs(z - x)
    yres = abs(z - y)
    if (xres == yres):
        return "Mouse C"
    elif xres < yres:
        return "Cat A"
    else:
        return "Cat B"
    

q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = catAndMouse(x, y, z)
    print(result)
