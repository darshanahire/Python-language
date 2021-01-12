n=int(input("Enter any no:"));
a=0
b=1
while(n-2):
	c=a+b;
	a=b
	b=c
	print(c," ")
	n=n-1