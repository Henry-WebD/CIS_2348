print("Enter amount of lemon juice (in cups):")
lemon_juice = int(input())
print("Enter amount of water (in cups):")
water = int(input())
print("Enter amount of agave nectar (in cups):")
agave_nectar = float(input())
print("How many servings does this make?")
servings = int(input())
print("")
print("Lemonade ingredients - yields " + '{:.2f}'.format(servings) + " servings")
print('{:.2f}'.format(lemon_juice) + " cup(s) lemon juice")
print('{:.2f}'.format(water) + " cup(s) water")
print('{:.2f}'.format(agave_nectar) + " cup(s) agave nectar")
print("")
print("How many servings would you like to make?")
user_servings = int(input())
print("")
print("Lemonade ingredients - yields " + '{:.2f}'.format(user_servings) + " servings")
new_lemon = (user_servings * lemon_juice) / servings
new_water = (user_servings * water) / servings
new_agave = (user_servings * agave_nectar) / servings
print('{:.2f}'.format(new_lemon) + " cup(s) lemon juice")
print('{:.2f}'.format(new_water) + " cup(s) water")
print('{:.2f}'.format(new_agave) + " cup(s) agave nectar")
print("")
print("Lemonade ingredients - yields " + '{:.2f}'.format(user_servings) + " servings")
lemon_gallons = new_lemon / 16
water_gallons = new_water / 16
agave_gallons = new_agave / 16
print('{:.2f}'.format(lemon_gallons) + " gallon(s) lemon juice")
print('{:.2f}'.format(water_gallons) + " gallon(s) water")
print('{:.2f}'.format(agave_gallons) + " gallon(s) agave nectar")
