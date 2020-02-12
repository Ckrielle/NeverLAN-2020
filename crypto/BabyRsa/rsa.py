from pwn import *
import gmpy
   
c = "2193 1745 2164 970 1466 2495 1438 1412 1745 1745 2302 1163 2181 1613 1438 884 2495 2302 2164 2181 884 2302 1703 1924 2302 1801 1412 2495 53 1337 2217".split()
e = 569
n = 2533
   
#Since n is really small, we can factor it in e.g. factorb
p = 17
q = 149

phi = (p-1) * (q-1)
d = gmpy.invert(e, phi)

m = ''
for i in c:
   m += chr(pow(int(i), d, n))

print(m)

