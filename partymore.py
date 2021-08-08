#Start by greeting the user
name = str(input("Hello! What's your name? "))
print("Hello", name + "!", "Let's see if it's time to leave this party.")
isAwkward = str(input("Is it awkward? ")) 
isFood = str(input("Is there free food? "))
if isAwkward == "no":
  print("Stay and par-tay")
elif isAwkward == "yes" and isFood == "yes":
# add some code that will print "Stay for the food!"  if both of these conditions are met" and otherwise print "Time to go home"
  print("Stay for the food!")
elif isAwkward =="yes" and isFood == "no":
  print("Time to go home")