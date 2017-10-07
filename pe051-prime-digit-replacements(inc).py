#pe051
import mathtools

l = mathtools.primelist(57000)
p = []

for i in l:
    if(len(str(i))==5):
        p.append(i)

print(p)
