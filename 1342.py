num = 14
step = 0
while num > 0:
    if num % 2 == 0:
        num /= 2
    else:
        num -=1
    step += 1
print(step)