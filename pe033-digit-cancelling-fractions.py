#(10*n+i)/(10*i+d) = n/d
#d(10*n + i) = n(10*i + d)
#n<d<i

prod_ntor = 1;
prod_dtor = 1;

for i in range(1,10):
    for d in range(1,i):
        for n in range(1,d):
            if d*(10*n + i) == n*(10*i + d):
                prod_ntor *= n;
                prod_dtor *= d;
print(prod_ntor/prod_dtor)
