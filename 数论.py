def egcd(a, b):
    """扩展欧几里得"""
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q

def get_inverse(mu, p):
    """
    获取y的负元
    """
    for i in range(1, p):
        if (i*mu)%p == 1:
            return i
    return -1

def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a
        m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r,u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def chinese_remainder(modulus, remainders):
    Sum = 0
    prod = reduce(lambda a, b: a*b, modulus)
    for n_i, a_i in zip(modulus, remainders):
        p = prod // n_i
        Sum += a_i * gmpy2.invert(p, n_i)*p
    return Sum % prod
