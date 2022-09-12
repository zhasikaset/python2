n = int(input("INPUT A NUMBER :"))
if n<=0 or n>10:
    print("PLEASE ENTER NUMBER BETWEEN 1 AND 10")
else:
    for i in range(10):
        print('{} * {} = {}'.format(n,i+1,n*(i+1)))
    