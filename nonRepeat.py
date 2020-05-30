def firstNonRepeat(s):
    a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for c in s:
            a[ord(c)-97] = a[ord(c)-97] + 1
    print(a)

    for i in range(26): # len(a) alphabet
        if a[i] == 1:
            return chr(i+97)

while True:
    s = input() # string of repeating & non repeating chars
    print(firstNonRepeat(s))
    
