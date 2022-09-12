n = int(input("Enter size of our R (n>=4) : "))
mtx,cnt = [],2
for i in range(n//2+1):
    row = ""
    if i == 0 or i == n//2:
        for j in range(n//2+1):
            row+="*"
    else:
        row+="*"
        for j in range(n//2):
            row+=" "
        row+="*"
    mtx.append(row)

for i in range(n//2):
    row = "*"
    for j in range(cnt):
        row+=" "
    row+="*"
    mtx.append(row)
    cnt+=1
for i in mtx:
    print(i)



