#This is a program which will tell the age

age =input("Please enter your age or the year you borned: ")
count = len(age)

if(count==2 or count==3): 
	age = int(age)
	if(age==0 or age<0):
		print("What the fuck man! You are not born yet.")
	elif(age>100 and age<200):
		print("You might be the oldest man alive on earth")
	elif(age>200):
		print("Man I have no words to say. You might be immortal")
	else:
		years_need = 100-age
		print(f"You will be 100 years old in {2019+years_need}") 

elif(count==4):
	age = int(age)
	if(age>2019):
		print("What the fuck man! you are not borned yet.")
	elif(age<1920 and age>1850):
		print("You might be the oldest man alive on earth")
	elif(age<1850):
		print("Man you might be immortal!")
	else:
		age_now = 2019-age
		years_need = 100 - age_now
		print(f"You will be 100 years old in {2019+years_need}")
