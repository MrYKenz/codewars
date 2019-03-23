### ATTEMPT 1 ###
f = 1
for i in range(1,n+1):
    f = f * i
s = str(f)[::-1]
zeros = 0
i = 0
while s[i] == '0':
    zeros += 1
    i += 1
print(zeros)

### ATTEMPT 2 ###
import math
len([i for i in str(math.factorial(n))[::-1] if i == '0'])

### ATTEMPT 3###
import math
a = len(math.factorial(n))-len(math.factorial(n).rstrip('0'))

##### FINAL SOLUTION ####
# REDUCE RUNTIME BY USING PRIME FACTOR 5 IN n! #
# Legendre's Formula A.K.A De Polignac's Formula #
def zeros(n):
    i = 5
    zeros = 0
    while n >= i:
        zeros += n // i
        i *= 5
    return zeros
