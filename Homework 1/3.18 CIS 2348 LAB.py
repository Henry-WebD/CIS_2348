print("Enter wall height (feet):")
wall_height = int(input())
print("Enter wall width (feet):")
wall_width = int(input())
area = wall_height * wall_width
print("Wall area: " + str(area) + " square feet")
paint1 = area / 350
print("Paint needed: " + '{:.2f}'.format(paint1) + " gallons")
can1 = round(paint1)
print("Cans needed: " + str(can1) + " can(s)")
color = {
    "red": 35,
    "blue": 25,
    "green": 23
}
print("")
print("Choose a color to paint the wall:")
user_color = input()
price = color[user_color] * can1
print("Cost of purchasing " + str(user_color) + " paint: $" + str(price))
