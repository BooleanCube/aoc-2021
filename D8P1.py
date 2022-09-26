s = 0
for i in range(200):
    inp, out = input().split(" | ")
    inp = inp.split()
    out = out.split()
    s += sum(1 for j in out if len(j)==2 or len(j)==3 or len(j)==4 or len(j)==7)
print(s)
