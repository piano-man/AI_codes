a=[];
def push(val):
	a.append(val);
def pop():
	if(len(a)):
		return a.pop(len(a)-1);
	return "EMPTY";
print("OPERATIONS:");
op = input();
for i in range(int(op)):
	print("push or pop:");
	inp = input();
	if(inp == "push"):
		val = input();
		push(val);
	else:
		print(pop());