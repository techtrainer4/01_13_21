# fname = input("Type your first name. ")

# lname = input("Type your last name.")

# age = input("Type your age.") #string input
# age = int(age) #turns strings to ints
# age = age + 1 #add one to that number

# print(f"{fname} {lname} is {age} years old.")

#conditionals
x = input("Pick a number, any number!")
x = float(x)

if x > 0 :
  print("That's a positive number.")
elif x == 0:
  print("That number is zero.")
# elif x < 0:
#   print("That's a negative number.")
else:
  print("That's a negative number.")

pet = "goldfish"
if pet == "cat":
  print("Does your cat sleep all day?")
elif pet == "dog":
  print("Does your dog like to fetch?")
else:
  print(f"So...what does a {pet} like to do?")

cookie = input("Do you like cookies?")
# if cookie == "Yes" or cookie == "yes" or cookie == "Yah":
if cookie != "No":
  print("Cookies are indeed awesome.")

"""

The weather in the winter is good if you like skiing
print("The weather is great now")

"""

print("The weather is great now")



