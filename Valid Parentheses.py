def valid_parentheses(string):
    #### return bool(string.count("(") == string.count(")") and len(string) in range(0,101))
    return [i for i in string if i is "(" or i is ")"]

print(valid_parentheses("hi())("))  
            
