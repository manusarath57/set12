n=[]
b=int(input("Enter number of elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    n.append(c)
n.sort()
print("Largest element is:",n[b-1])
