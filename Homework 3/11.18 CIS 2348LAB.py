#Henry Saravia, PSID: 1853318


nums = list(map(int, input().split()))
nums.sort()
for i in nums:
    if i >= 0:
        print(i, end=' ')
