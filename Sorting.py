n=int(input("enter the length of list"))
list=[]
i=0
while i<n:
    numbers=int(input("enter the number here:"))
    list.append(numbers)
i=i+1
list.sort()
print("the list of numbers are:",list)