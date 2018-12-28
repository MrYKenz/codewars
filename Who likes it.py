def likes(names):
    if len(names) == 0: return "no one likes this"
    elif len(names) == 1: return names[0] + " likes this"
    elif len(names) == 2: message = names[0] + " and " + names[1]
    elif len(names) == 3: message = names[0] + ", " + names[1] + " and " + names[2]
    else: message = "%s, %s and %d others" % (names[0],names[1],len(names[2:])) #or len(names)-2

    return message + " like this"

print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
