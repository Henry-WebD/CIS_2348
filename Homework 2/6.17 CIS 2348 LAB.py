user_password = input()
new_password = ''

for i in user_password :
    if (i =='i'):
        new_password += "!"
    elif (i =='a'):
        new_password += "@"
    elif (i == 'm'):
        new_password += "M"
    elif (i == 'B'):
        new_password += "8"
    elif (i == 'o'):
        new_password += "."
    else:
        new_password += i
print(new_password + "q*s")