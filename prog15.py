n=int(input("Enter a number:"))
fact=1
if n>0:
	for i in range(1,n+1):
		fact=fact*i
	print("factorial:",fact)
else:
	print("invalid")
