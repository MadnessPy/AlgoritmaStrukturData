def insertSort(arr):
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j>= 0 and key < arr[j] : 
			arr[j + 1] = arr[j]
			j-= 1
		arr[j + 1] = key


arr = [12,11,13,5,6,10]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])

nilai uts = [
	{"nama":"Siti Azizah","nilai":85},
	{"nama":"Siti Aminah","nilai":95},
	{"nama":"Siti fatimah","nilai":85},
	{"nama":"Siti maimunah","nilai":85},
	{"nama":"Siti komariah","nilai":85},
]
def pengurutan(nilai_uts):
	for i in range(len(nilai_uts)):
		a = nilai_uts[i]["nilai"]
		b = nilai_uts[i]["nama"]
		j = i
		while j>0 and x<nilai_uts[j-1]["nilai"]:
			nilai_uts[j]["nilai"] - nilai_uts[j 1]["nilai"]
			nilai_uts[j]["nama"] - nilai_uts[j 1]["nama"]
			j -=1
		nilai_uts[j]["nilai"] = a
		nilai_uts[j]["nama"] = b
	return nilai_uts

nilai_uts = pengurutan(nilai_uts)
for i in range(len(nilai_uts)):
	print("%s"%nilai_uts[i])