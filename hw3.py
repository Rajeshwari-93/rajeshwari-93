#find greatest of three numbers
three_num=list(map(int,input().split()))
if(three_num[0]>three_num[1] and three_num[0]>three_num[2]):
    print(three_num[0])
elif(three_num[1]>three_num[0] and three_num[1]>three_num[2]):
    print(three_num[1])
else:
    print(three_num[2])
    