s = 0
for k in range(200):
    inp, out = input().split(" | ")
    inp = sorted(["".join(sorted(j)) for j in inp.split()], key=len)
    out = ["".join(sorted(j)) for j in out.split()]
    dict = {}
    dict[1] = inp[0]
    dict[7] = inp[1]
    dict[4] = inp[2]
    dict[8] = inp[-1]
    dict[inp[0]] = 1
    dict[inp[1]] = 7
    dict[inp[2]] = 4
    dict[inp[-1]] = 8
    l = [i for i in dict[4] if i not in dict[1]]
    for i in range(3,6):
        if l[0] in inp[i] and l[1] in inp[i]: dict[inp[i]] = 5
        elif dict[1][0] in inp[i] and dict[1][1] in inp[i]: dict[inp[i]] = 3
        else: dict[inp[i]] = 2
    for i in range(6, 9):
        if l[0] not in inp[i] or l[1] not in inp[i]: dict[inp[i]] = 0
        elif sum(1 for j in dict[4] if j in inp[i])==4: dict[inp[i]] = 9
        else: dict[inp[i]] = 6
    s += int("".join([str(dict[i]) for i in out]))
print(s)
