# Henry Saravia, PSID: 1853318

players = {}
x = 1
count = 1

for x in range(1, 6):
    jersey = int(input('Enter player {}\'s jersey number:\n'.format(x)))
    rating = int(input('Enter player {}\'s rating:\n\n'.format(x)))

    if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:
        print("error - invalid entry")
        break

    else:
        players[jersey] = rating

print("ROSTER")

for jersey, rating in sorted(players.items()):
    print("Jersey number: %d, Rating: %d" % (jersey, rating))

user_choice = ''

while user_choice.upper() != 'Q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr'
          ' - Output players above a rating\no - Output roster\nq - Quit\n')

    user_choice = input('Choose an option:\n')

    if user_choice == 'a':
        jersey = int(input('Enter a new player\'s jersey number:\n'.format(x)))
        rating = int(input('Enter the players\'s rating:'.format(x)))
        players[jersey] = rating

    elif user_choice == 'd':
        jersey = int(input('Enter a jersey number:'))
        if jersey in players.keys():
            del players[jersey]

    elif user_choice == 'u':
        jersey = int(input('Enter a jersey number: '))
        if jersey in players.keys():
            rating = int(input('Enter a new rating for player: '))
            players[jersey] = rating


    elif user_choice == 'r':
        input_rating = int(input('Enter a rating'))
        print('ABOVE {}'.format(input_rating))

        for jersey, rating in sorted(players.items()):
            if rating > input_rating:
                print("Jersey number: %d, Rating: %d" % (jersey, rating))

    elif user_choice == 'o':
        print("ROSTER")
        for jersey, rating in sorted(players.items()):
            print("Jersey number: %d, Rating: %d" % (jersey, rating))
