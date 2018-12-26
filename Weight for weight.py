strng = "56 65 74 100 99 68 86 180 90"

# print([sum([int(x) for x in i]) for i in weights.split()])

def order_weight(strng):
    array = sorted(strng.split(' '))
    return " ".join(sorted(array, key=weights))


def weights(key):
    return sum([int(x) for x in key])

print(order_weight(strng))



