x= str(input()).split()
m,n = int(x[0]),int(x[1])
y = m*n

if y%2==0:
    print(int(y/2))
else:
    print(int((y-1)/2))