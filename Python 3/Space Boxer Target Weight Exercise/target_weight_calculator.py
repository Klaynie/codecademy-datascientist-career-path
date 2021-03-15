print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  target_weight = 0.91 * weight
  print("Your target weight for Venus is: " + str(target_weight))
elif planet == 2:
  target_weight = 0.38 * weight
  print("Your target weight for Mars is: " + str(target_weight))
elif planet == 3:
  target_weight = 2.34 * weight
  print("Your target weight for Jupiter is: " + str(target_weight))
elif planet == 4:
  target_weight = 1.06 * weight
  print("Your target weight for Saturn is: " + str(target_weight))
elif planet == 5:
  target_weight = 0.92 * weight
  print("Your target weight for Uranus is: " + str(target_weight))
elif planet == 6:
  target_weight = 1.19 * weight
  print("Your target weight for Neptune is: " + str(target_weight))
else:
  print("I do not have information for this planet!")
