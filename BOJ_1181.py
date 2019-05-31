n = int(input())

dicts = {}
for i in range(n):
	w = input()
	dicts[w] = len(w)

keys = list(dicts.keys())
values = list(dicts.values())

res = sorted(keys, key=lambda x: (len(x), x))
for i in res:
	print(i)