sum , cnt = 0 , 0
n = int(input())
while n!=0:
    sum+=n
    cnt+=1
    n = int(input())
if cnt==0:
    print("ENTER AT LEAST ONE NUMBER")
else:
    print('sum is : {} , and average is : {} . '.format(sum,sum/cnt))