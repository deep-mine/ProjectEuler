#totient(n) = n(1-1/p1)(1-1/p2)...
import primecache

prime_list = primecache.primelist(100)

num = 1
ind = 0

while num <1000000:
    num *= prime_list[ind]
    ind += 1
print(num/prime_list[ind-1])
