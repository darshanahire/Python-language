n=int(input("Enter any number :"));
cube=0;
temp=n;
while(n>0):
	no=n%10
	cube=cube+(no**3)
	n=n//10
if(temp==cube):
	print("No is armstrong")
else:
	print("No is not armstrong")
