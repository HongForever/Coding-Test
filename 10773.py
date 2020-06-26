# data = list(map(int, input.split()))
data=[1,3,5,4,0,0,7,0,0,6]
result=[]
sum=0

for i in data:
    if i != 0:
        result.append(i)    
    else:
        result.pop()
print(result)

for j in result:
    sum += j
print(sum)