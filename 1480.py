nums = [1,2,3,4]
answer = [nums[0]]
for i in range(1,len(nums)):
    answer.append(nums[i] + answer[i-1])
print(answer)