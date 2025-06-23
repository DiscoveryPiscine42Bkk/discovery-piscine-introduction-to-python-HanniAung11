org = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in org:
    if i > 5:
        new.append(i + 2)

res = []

for j in new:
    duplicate = False
    for k in res:
        if j == k:
            duplicate = True
            break
    if not duplicate:
        res.append(j)

print(res)
