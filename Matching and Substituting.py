import re

def change(s, prog, version):
    data = "Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01"
    match = re.match(r'^(\d{1,2}).(\d{1,2})$', version)
    match2 = re.match(r'^(\d{1,2}).(\d{1,2})$', s.split('\n')[5][9:])
    match3 = re.match(r'^1-(\d{3})-(\d{3})-(\d{4})$', s.split('\n')[3][8:])
    if s.split('\n')[5][9:] == "2.0":
            version = s.split('\n')[5][9:]
    if not match:            
            if not match2 and len(version) == 1:
                return "ERROR: VERSION or PHONE"
    if not match2:
        return "ERROR: VERSION or PHONE"
    if not match3:
        return "ERROR: VERSION or PHONE"
    return "Program: %s %s Version: %s" % (prog,data,version)

s = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-009\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
print(change(s, "Ladder", "1.5.6"))


