# 2.  mengurutkan nim
def insertion_sort(a):
	for i in range(len(a)):
		nim=a[i]["nim"]
		j=i
		while j>0 and nim < a [j-1]["nim"]:
			a[j]["nim"]=a[j-1]["nim"]
			j-=1
		a[j]["nim"]=nim
	return a

def binary_search(a,n):
	first=0
	last=len(a)-1
	found = False
	while first<= last and not found:
		mid=(first+last)//2
		if a[mid]["nim"]==n:
			found = True
			print("found on index %s"%mid)
		else:
			if n < a[mid]["nim"]:
				last=mid-1
			else:
				first = mid+1
	return found

a = [{"nim":18012,"nama":"Fulan"},
	{"nim":18002,"nama":"Fulana"},
	{"nim":18008,"nama":"Fulani"},
	{"nim":18005,"nama":"Anton Antoni"},
	{"nim":18010,"nama":"Ricky Rich"},]
print(binary_search(a,18010))
print(binary_search(a,18005))

a = insertion_sort(a)

for i in range(len(a)):
    print("%s"%a[i])

