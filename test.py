t = [['a', 'b'], ['a', 'c'], ['c', 'c'], ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'f']]

print(t)

	
result = []
new = []

for item in t:
#	print(item)

	if 'f' in item:
#		print(item)
		result = result + item
		print(result)
#		t.remove(item)
	else:
		new.append(item)

print(result)
print(new)
