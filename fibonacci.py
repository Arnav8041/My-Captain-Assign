length=int(input('input the length of the fibonacci series:'))
cnt1,cnt2=0,1
sum_=0
for i in range(0,length):
    
    cnt1=cnt2
    cnt2=sum_
    sum_=cnt1+cnt2
    print(sum_,end='')


