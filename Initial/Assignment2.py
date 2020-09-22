n = int(input())
socks = list(map(int, input().split()))
count = 0
pairs = set()

for i in socks:
    if i in pairs:
        pairs.remove(i)
        count += 1
    else:
        pairs.add(i)

print(count)
