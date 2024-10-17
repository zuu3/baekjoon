T = int(input())

for _ in range(T) :
    str = input()
    stack = []
    for c in str :
        if (c == '(') :
            stack.append('(')
        elif (c == ')') :
            if stack :
                stack.pop()
            else :
                print("NO")
                break
    else :
        if not stack : print("YES")
        else : print("NO")
                
            