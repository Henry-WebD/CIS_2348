def exact_change(user_total):
    dollar = user_total // 100
    user_total %= 100
    quarter = user_total // 25
    user_total %= 25
    dime = user_total // 10
    user_total %= 10
    nickel = user_total // 5
    user_total %= 5
    penny = user_total
    return dollar, quarter, dime, nickel, penny
if __name__ == '__main__':
    input_x = int(input())
    input_dollar, input_quarter, input_dime, input_nickels, input_penny = exact_change(input_x)
    if input_x <= 0:
        print('no change')
    else:
        if input_dollar > 1:
            print('%d dollars' % input_dollar)
        elif input_dollar == 1:
            print('%d dollar' % input_dollar)

        if input_quarter > 1:
            print('%d quarters' % input_quarter)
        elif input_quarter == 1:
            print('%d quarter' % input_quarter)

        if input_dime > 1:
            print('%d dimes' % input_dime)
        elif input_dime == 1:
            print('%d dime' % input_dime)

        if input_nickels > 1:
            print('%d nickels' % input_nickels)
        elif input_nickels == 1:
            print('%d nickel' % input_nickels)

        if input_penny > 1:
            print('%d pennies' % input_penny)
        elif input_penny == 1:
            print('%d penny' % input_penny)




