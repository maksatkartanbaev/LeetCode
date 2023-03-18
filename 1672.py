accounts = [[1,5],[7,3],[3,5]]
wealth = []
for i in accounts:
    wealth.append(sum(i))
print(max(wealth))