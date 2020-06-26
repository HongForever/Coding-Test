import sys
sys.setrecursionlimit(1000000)

n,m = map(int, input.split())
data = list(map(int, input.split()))

result = 0
length = len(data)

for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            sum = data[i]+data[j]+data[k]
            if sum > m:
                continue
            else:
                result = max(result, sum)

print(result)