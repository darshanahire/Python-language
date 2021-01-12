import random;
print("Welcome to the game of gessing the number");
print("Enter any number between 0-10");

i=0;
def game(gum):
	num=random.randint(0,10);
	print (num)
	global i;
	while(i<100):
 	 	no=int(input(">>"));
 	 
	  	if (no==num):
		 	 print("Yes that the number\n\n");
		 	 char=input("If you want to play again Enter 'Y' \n>>"); 
		 	 if (char=='Y' or char=='y'):
		 	 	print("Welcome again to the game of gessing the number");
		 	 	print("Enter any number brtween 0-10")
		 	 	game(11);
		 	 else:
				  print("Thank you....")
				  i=111
				  break;
	  	elif(no>num):
		  	print("number is smaller than you enterd");
	  	else:
	 		 print("number is gretter than you enterd");
	  	i=i+1;	
game(8)