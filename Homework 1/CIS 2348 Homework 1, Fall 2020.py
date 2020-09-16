from datetime import datetime

print("Please input the current date in the following format:")
print("(MM)")
print("(DD)")
print("(YYYY)")
user_current_month = int(input())
user_current_day = int(input())
user_current_year = int(input())

print("Please input your date of birth in the following format:")
print("(MM)")
print("(DD)")
print("(YYYY)")
user_bday_month = int(input())
user_bday_day = int(input())
user_bday_year = int(input())

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

if ( (currentMonth == user_bday_month) and (currentDay == user_bday_day) ) :
    print("")
    print("")

    age = user_current_year - user_bday_year - (
                (user_current_month, user_current_day) < (user_bday_month, user_bday_day))

    print("Birthday Calculator")
    print("Current Day")
    print("Month: " + str(user_current_month))
    print("Day: " + str(user_current_day))
    print("Year: " + str(user_current_year))
    print("Birthday")
    print("Month: " + str(user_bday_month))
    print("Day: " + str(user_bday_day))
    print("Year: " + str(user_bday_year))
    print("You are " + str(age) + " years old.")
    print("---------------------------------------------------")
    print("Look's like today is your Birthday....")
    print("HAPPY BIRTHDAY!!!!!")

else:
    print("")
    print("")

    age = user_current_year - user_bday_year - (
                (user_current_month, user_current_day) < (user_bday_month, user_bday_day))

    print("Birthday Calculator")
    print("Current Day")
    print("Month: " + str(user_current_month))
    print("Day: " + str(user_current_day))
    print("Year: " + str(user_current_year))
    print("Birthday")
    print("Month: " + str(user_bday_month))
    print("Day: " + str(user_bday_day))
    print("Year: " + str(user_bday_year))
    print("You are " + str(age) + " years old.")









