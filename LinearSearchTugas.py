#1. liner search [1,2,3,4,5,6,7,8,9,19] n=8
def linear_search(myList,item):
    for i in range(len(myList)):
        if myList[i]==item:
            return i
    return -1
 
myList = [1,2,3,4,5,6,7,8,9,19]
print("Element in List :", myList)
x = 8
#int(input("enter searching element :"))
 
result = linear_search(myList,x)
if result==-1:
     print("Element not found in the list")
else:
     print( "Element " + str(x) + " is found at position %d" %(result))

