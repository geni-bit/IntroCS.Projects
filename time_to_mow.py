# IntroCS Project 1 - Tasks #3

# Ask the user the depth of a lawn (in feet)
depth = int(input("Please enter the depth of the lawn(in feet): "))

# Ask the user the width of a lawn (in feet)
width = int(input("Please enter the width of the lawn(in feet): "))
# Variable for the time (hours) it will  mow a lawn
time = ((depth * width)/2)/3600

# The Variable for the total the cost for mowing the lawn
totalcost = float(time * 20)

# The report of how long it will take to mow the lawn and total cost
print("It will take" , time ,"hours to mow the lawn.")
print("The total cost for mowing the lawn would be $" , round(totalcost,2))
