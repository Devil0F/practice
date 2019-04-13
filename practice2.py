m = int(raw_input())
temp = []
for _ in range(m):
	line = [list(map(int,item.split(','))) for item in raw_input().split(';')]
	temp.extend(line)

temp = sorted(temp,key=lambda x:x[0])
ret = [temp[0]]
for item in temp[1:]:
	if ret[-1][1] >= item[0]:
		ret[-1][1] = max(ret[-1][1],item[1])
	else:
		ret.append(item)
s = ''
for item in ret[:-1]:
	s += str(item[0]) + ',' + str(item[1]) + ';'
s += str(ret[-1][0]) + ',' + str(ret[-1][1])

print(s)
