def valid_parentheses(string):
    #### return bool(string.count("(") == string.count(")") and len(string) in range(0,101))
    count = 0
    for i in string:
        if i == "(": count += 1
        elif i == ")": count -= 1
        if count < 0: return False
    return count == 0

print(valid_parentheses("hi())("))  
            
