#Logical operator example
age1 = int(input("Enter age1"))
age2 = int(input("Enter age2"))

if (age1 == 12) and (age2 == 12):
	print("both the ages are equal!")
elif age1 == 12 or age2 == 20:
	print("Any one age is 12")
elif not age1 == 12:
	print("no response")
