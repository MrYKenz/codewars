def meeting(s):
    s = s.split(';')
    y = []
    for i in s:
        x = i.split(':')
        x[0],x[1] = x[1].upper(), x[0].upper()
        y.append(tuple(x))
    return ''.join(str(i) for i in sorted(y)).replace("\'","")

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))

