def is_valid_IP(strng):
    ip = strng.split('.')
    if len(ip) != 4: return False
    for i in ip:
        if not i.isdigit() or int(i) > 255 or int(i) < 0 or (len(i) > 1 and i[0] == '0'): return False
    return True
        
print(is_valid_IP('212.255.56.0'))
