def ips_between(ip1,ip2):
    ip1 = [int(i) for i in ip1.split('.')]
    ip2 = [int(i) for i in ip2.split('.')]
    ip1[0] *= 16777216
    ip2[0] *= 16777216
    ip1[1] *= 65536
    ip2[1] *= 65536
    ip1[2] *= 256
    ip2[2] *= 256
    return sum(ip2) - sum(ip1)

print(ips_between("10.0.0.0", "10.0.1.0"))
