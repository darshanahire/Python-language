import random
list=[0,1,2,3,4,5,6,7,8,9]
i=0;
no=[]
flag=0
while(i<30):
	num=random.randint(0,9)
	if (set(list)==set(no)):
    	 break;
	if num in no:
		flag;
	else:
    	 no.append(num)
	i=i+1
print(no)

	
	