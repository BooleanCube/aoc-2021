crabs = list(map(int,input().split(",")))
print(min([sum(abs(crabs[a]-crabs[b]) for b in range(len(crabs))) for a in range(len(crabs))]))
