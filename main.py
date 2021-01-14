import random
print(random.randint(1,6))

money = 100
while money >= 5:
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  if die1 == 6 and die2 == 6:
    money = money + 20
    print(f"You have ${money} left.")
  else:
    money = money - 5
    print(f"You have ${money} left.")
if money <= 0:
  print("You're all out. Go home.")


















