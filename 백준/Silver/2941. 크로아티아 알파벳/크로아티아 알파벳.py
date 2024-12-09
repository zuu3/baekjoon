s = input()
ans = 0
i = 0

while i < len(s):
    if s[i] == 'c':
        if i + 1 < len(s) and (s[i+1] == '=' or s[i+1] == '-'):
            ans += 1
            i += 2
            continue
    elif s[i] == 'd':
        if i + 1 < len(s) and s[i+1] == '-':
            ans += 1
            i += 2
            continue
        elif i + 2 < len(s) and s[i+1] == 'z' and s[i+2] == '=':
            ans += 1
            i += 3
            continue
    elif s[i] == 'l':
        if i + 1 < len(s) and s[i+1] == 'j':
            ans += 1
            i += 2
            continue
    elif s[i] == 'n':
        if i + 1 < len(s) and s[i+1] == 'j':
            ans += 1
            i += 2
            continue
    elif s[i] == 's':
        if i + 1 < len(s) and s[i+1] == '=':
            ans += 1
            i += 2
            continue
    elif s[i] == 'z':
        if i + 1 < len(s) and s[i+1] == '=':
            ans += 1
            i += 2
            continue
    ans += 1
    i += 1

print(ans)