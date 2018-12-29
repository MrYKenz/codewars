import re

def validate_pin(pin):
    # return re.match(r'^(?=(?:.{4}|.{6})$)(\d)*$', pin) != None
    return re.fullmatch("\d{4}|\d{6}", pin) != None

### Shoulda Coulda Woulda ### len(pin) in (4, 6) and pin.isdigit()
