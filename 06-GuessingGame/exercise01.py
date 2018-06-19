from random import randint
compChoice = int(randint(0,5))
print(f"computer choice is {compChoice}")

while True:
	num = int(input("Guess you number!!"))
	if num == compChoice:
		print("your number is equal to computer choice!")
		break
	elif num < compChoice:
		print("your number is smaller than computer choice!")
	else :
		print("your number is greater than computer choice!")
