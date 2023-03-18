nums = [1, 2, 3, 5, 6, 7]
answer = []
n = len(nums)
for i in range(1, n + 1):
    if i not in nums:
        answer.append(i)
print(answer)
