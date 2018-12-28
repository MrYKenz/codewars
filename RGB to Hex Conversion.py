def rgb(r, g, b):
    arr = []
    for i in [r,g,b]:
        if i < 0: arr.append(0)
        elif i > 255: arr.append(255)
        else: arr.append(i)
    return "".join(num if len(num) > 1 else "0" + num for num in [hex(j)[2:].upper() for j in arr])

print(rgb(-20,255,2))
    
