import primecache

limit = 1000000
prime_list = primecache.primelist(limit)

prime_sum = [0]*(len(prime_list)+1)
prime_sum[0] = 0
for i in range(len(prime_list)):
    prime_sum[i+1] = prime_sum[i] + prime_list[i]

# print(prime_list)
# print(prime_sum)

longest_chain = 0
ans = 0


for i in range(len(prime_sum)-1,0,-1):
    for j in range(0,i-longest_chain):
        chain = 0
        if prime_sum[i]-prime_sum[j] < limit and prime_sum[i]-prime_sum[j] in prime_list:
            chain = i-j
            # print(prime_sum[i],prime_sum[j],prime_sum[i]-prime_sum[j],chain)
            if chain > longest_chain:
                longest_chain = chain
                ans = prime_sum[i]-prime_sum[j]
            break
print(ans,longest_chain)
