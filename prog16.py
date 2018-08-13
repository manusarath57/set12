a=int(input('Enter the number: \n'))
temp=a
result=0
while(temp!=0):
	b=temp%10
	result=result + b*b*b
	temp=temp/10
if(result==a):
	print(' amstrong number')
else:
	print(' not an amstrong number')
