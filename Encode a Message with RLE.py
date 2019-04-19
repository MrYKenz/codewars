from re import sub

def encode(inp):
    return sub(r'(.)\1*', lambda x: x.group(1) + str(len(x.group(0))), inp)
