def num_interesting(number):    

    if number % 100 == number:
        return False
        
    elif number % 100 == 0:
        return True
    
    elif len(set(str(number))) == 1:
        return True
    
    elif str(number)[::-1] == str(number):
        return True
        
    elif str(number) in '1234567890' or str(number) in '9876543210':
        return True
    
def is_interesting(number, awesome_phrases):
    if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
        
    elif number in awesome_phrases:
        return 2
        
    elif num_interesting(number):
        return 2
        
    elif num_interesting(number + 1) or num_interesting(number + 2):
        return 1
    
    return 0


print(is_interesting(12345,[]))
print(is_interesting(1235321,[]))
print(is_interesting(1336,[1337]))
