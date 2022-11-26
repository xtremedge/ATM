print("Welcome to United Bank ATM")
restart=("Y")
chances = 3
balance = 50.46
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit PIN:'))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance \n')
            print('Please Press 2 To make Withdrawl \n')
            print('Please Press 3 To Pay in \n')
            print('Please Press 4 To Return Card \n')
            option = int(input('What Would you like to Choose?'))
            if option == 1:
                print('Your Balance is $', balance, "\n")
                restart = input('Would You like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input('How much would you like to withdraw? \n $10/$20/$30/$50/$80/$100 for other enter 1:'))
                if withdrawl in [10, 20, 30, 50, 80, 100]:
                    balance = balance - withdrawl
                    print('\nYour Balance is now $',balance)
                    restart = input('Would you like to go back?')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 30, 50, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired Amount:'))
            elif option == 3:
                Pay_in = float(input())