n = int(input("Enter size of our O (n>=4) : "))
mtx = [[""] for i in range(n)]
for i in range(n):
    if i==0 or i==n-1:
        mtx[i]+=" "
        for j in range(n-2):
            mtx[i]+="*"
        mtx[i]+=" "
    else:
        mtx[i]+="*"
        for j in range(n-2):
            mtx[i]+=" "
        mtx[i]+="*"
for i in mtx:
    for j in i:
        print(j,end = "")
    print()