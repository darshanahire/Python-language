x=int(input("Enter the number of element of list: "))
l1=[]
def input_fun():
    for i in range(0,x):
        if(i==0):
            num=int(input('Enter 1st element: '))
            l1.append(num)
        elif(i==1):
            num=int(input('Enter 2nd element: '))
            l1.append(num)
        elif(i==2):
            num=int(input('Enter 3rd element: '))
            l1.append(num)
        else:
            num=int(input('Enter {}th element: '.format(i+1)))
            l1.append(num)
def swap(a,b):
    l1[j],l1[j+1]=l1[j+1],l1[j]
input_fun()
for i in range(0,x-1):
    for j in range(0,x-1):
        if (l1[j]>l1[j+1]):
            swap(l1[j],l1[j+1])
print(l1)