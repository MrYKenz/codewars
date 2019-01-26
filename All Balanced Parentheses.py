def balanced_parens(n):
    a = []
    def parens(left, right, s):
        if right == n:
            a.append(s)
        if left < n:
            parens(left + 1, right, s + "(")
        if right < left:
            parens(left, right + 1, s + ")")
    parens(0, 0, "")
    return a
    
print(balanced_parens(3))
