crabs=list(map(int,input().split(",")))
print(min([sum([(abs(a-b)*(abs(a-b)+1)//2) for a in crabs]) for b in range(0,max(crabs)+1)]))
