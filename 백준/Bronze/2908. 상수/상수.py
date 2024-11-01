a,b = input().split()
na = ''
nb = ''
for c in a :
    na = c + na
for c in b :
    nb = c + nb
if (int(na) > int(nb)) : print(na)
else : print(nb)