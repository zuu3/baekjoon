n = int(input())

for _ in range(n):
    txt = input().strip()
    txt_lower = txt.lower()
    
    if txt_lower == txt_lower[::-1]:
        print("Yes")
    else:
        print("No")