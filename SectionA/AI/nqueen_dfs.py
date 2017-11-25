
col = []
dig1 = []
dig2 = []
arr = []
n = (int)(input())
for i in range(0, n):
	col.append(0)
	arr.append(-1)
for i in range(0, 2 * n):
	dig1.append(0)
	dig2.append(0)

def feasible(r, c):
	if(col[c] == 1):
		return False
	if(dig1[r + c] == 1):
		return False
	if(dig2[r - c + n] == 1):
		return False
	return True
def nqueen(r):
	if r == n:
		return True

	for i in range(0, n):
		if(feasible(r, i)):
			arr[r] = i
			col[i] = 1
			dig1[r + i] = 1
			dig2[r - i + n] = 1
			if(nqueen(r + 1)):
				return True
			arr[r] = -1
			col[i] = 0
			dig1[r + i] = 0
			dig2[r - i + n] = 0
	return False

if(nqueen(0)):
	for i in range(0, n):
		for j in range(0, n):
			if arr[i] == j:
				print("Q ", end = "")
			else :
				print("0 ", end = "")
		print()