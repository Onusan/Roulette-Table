import random

print('-' * 50)
print('Welcome to roulette table')
print('-' * 50)

user_Bal_is_true = False

while not user_Bal_is_true:
    try:
        user_Bal = int(input('Enter the amount to deposit: $'))
        if user_Bal > 0:
            user_Bal_is_true = True
        else:
            print('The amount deposit needs to be higher than 0.')
    except ValueError:
        print('Enter a numeric amount like 100.')

print('-' * 50)
print('Let the betting begin')
print('-' * 50)


game_playing = True
winnings = []

while game_playing:

    betting_amount_vaild = False
    
    while not betting_amount_vaild: 
        try:
            betting_amount = float(input('Enter the amount to bet: $'))
            if betting_amount <= user_Bal + sum(winnings) and betting_amount > 0:
                betting_amount_vaild = True
            else:
                print('The betting amount needs to be higher than 0, or can not be greater than your initial deposit.')
        except ValueError:
            print('Enter a numeric amount like 100.')

    betting_option_vaild = False

    while not betting_option_vaild:
        try:
            betting_option = input('Do you want to bet even/odd or black/red: ')
            if betting_option.lower() == 'even' or  betting_option.lower() == 'odd' or betting_option.lower() == 'black' or betting_option.lower() == 'red':
                betting_option_vaild = True
            else:
                print('Please choose one of the four betting options.')
        except ValueError:
            print('Please do not enter any numeric values or symbols.')

    winning_option = random.randint(0, 37)

    if (winning_option % 2 == 0):
        even_or_odd = 'even'
        black_or_red = 'red'
    else:
        even_or_odd = 'odd'
        black_or_red = 'black'

    print('The number is,', winning_option, even_or_odd, black_or_red)

    winning = 0

    if betting_option.lower() == black_or_red:
        winning = betting_amount * .3
    else:
        winning -= betting_amount

    if winning > 0:
        print('You won: $',betting_amount)
        winnings.append(winning)
        user_Bal += sum(winnings)
        print('Your total balance is now:$',"{:.2f}".format(user_Bal))
    else:
        print('You lost: $',betting_amount)
        winnings.append(winning)
        user_Bal += sum(winnings)
        print('Your total balance is now:$',"{:.2f}".format(user_Bal))

    if user_Bal <= 0:
      print('The house wins and you lose')
      break

    Replay_Vaild = False

    while not Replay_Vaild:
      replay_option = input('Do you wish to bet again Y or N: ')
      if replay_option.lower() == 'y':
        Replay_Vaild = True
      else:
        print('We wish to see you again.')
        game_playing = False
        Replay_Vaild = True