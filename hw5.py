my_list=list(map(int,input().split()))
temp=0
for i in range(len(my_list)):
    if(my_list[i]<temp):
        temp=my_list[i]
print(temp)