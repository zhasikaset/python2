n = int(input("Input a dog's age in human years: "))
cnt = 0
for i in range(1,n+1):
    if i<=2 :
        cnt+=10.5
    else:
        cnt+=4
print("The dog's age in dog's years is "+str(int(cnt)))