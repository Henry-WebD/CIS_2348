#Henry Saravia, PSID: 1853318

x1 = int(input())
y1 = int(input())
num1 = int(input())

x2 = int(input())
y2 = int(input())
num2 = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if x1 * x + y1 * y == num1 and x2 * x + y2 * y == num2:
            print(x, y)
            solution_found = True

if not solution_found:
    print("No solution")
