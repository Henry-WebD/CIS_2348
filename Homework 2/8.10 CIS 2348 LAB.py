#Henry Saravia, PSID: 1853318

x = input()
y = 0
z = len(x)-1
check = True
while(y<z):
    if(x[y] == ' '):
        y += 1
    elif(x[z] == ' '):
        z -= 1
    elif(x[y] != x[z]):
        check = False
        break
    else:
        y += 1
        z -= 1
if (check):
    print(x + " is a palindrome")
else:
    print(x + " is not a palindrome")
