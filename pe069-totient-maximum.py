#totient(n) = n(1-1/p1)(1-1/p2)...
import primecache

prime_list = primecache.primelist(600000)

# def primefactors(num):
#     pf = []
#     while num > 1:
#         for p in primes:
#             while num%p==0:
#                 num = num/p
#                 if p not in pf:
#                     pf.append(p)
#         break
#     return pf

def primefactors(num):
    pf = []
    i = 0
    while num>1:
        if num%prime_list[i]==0:
            while num%prime_list[i]==0:
                num/=prime_list[i]
                if prime_list[i] not in pf:
                    pf.append(prime_list[i])
            i += 1
        else:
            i += 1
    return pf

def totient(num):
    tot = num
    for i in primefactors(num):
        tot *= (1-1/i)
    return round(tot)

print(primefactors(24))

maxtotientfraction = -1
num = 0
for i in range(2,600000):
    fraction = i/totient(i)
    if fraction > maxtotientfraction:
        maxtotientfraction = fraction
        num = i
print(maxtotientfraction,num)
