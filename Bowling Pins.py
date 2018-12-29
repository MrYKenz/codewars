def bowling_pins(arr):
    backrow = " ".join(" " if i in arr else "I" for i in range(7,11)).center(7)
    midback = " ".join(" " if i in arr else "I" for i in range(4,7)).center(7)
    midfront = " ".join(" " if i in arr else "I" for i in range(2,4)).center(7)
    front = " ".center(7) if 1 in arr else "I".center(7)
    return "{}\n{}\n{}\n{}".format(backrow, midback, midfront, front)

print(bowling_pins([5]))
