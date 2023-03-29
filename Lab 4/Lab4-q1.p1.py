import random as rand
sum=0.00
for i in range(1000):
    randomNumber=rand.randint(1,1000)
    sum=sum+randomNumber
    avg=sum/1000
print(sum)
print(avg)
