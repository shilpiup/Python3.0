print("rock")
print("paper")
print("scissors")
print("Hello\n"*10)
name1 = input("Player name1?")
var1 = input("Player 1 choice?")
name2 = input("Player name2?")
var2 = input("Player 2 choice?")


if var1 == "rock" and var2 == "paper":
	print("Winner:" + name2)
elif var1 == "paper" and var2 == "rock":
	print("Winner:" + name1)
if var1 == "paper" and var2 == "scissors":
	print("Winner:" + name2)
if var1 == "scissors" and var2 == "paper":
	print("Winner:" + name1)
if var1 == "rock" and var2 == "scissors":
	print("Winner:" + name1)
if var1 == "scissors" and var2 == "rock":
	print("Winner:" + name2)
