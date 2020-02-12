from pwn import *
import gmpy

if __name__ == '__main__':
   
    c = 21931745216497014662495143814121745174523021163218116131438884249523022164218188423021703192423021801141224955313372217
    e = 569
    n = 2533
   
    #Since n is really small, we can factor it in e.g. factorb
    p = 17
    q = 149

    phi = (p-1) * (q-1)
    d = gmpy.invert(e, phi)

    end = hex(pow(c, d, n))
    print(str(end))

