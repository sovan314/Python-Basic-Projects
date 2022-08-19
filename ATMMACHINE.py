print("Welcome to BBC Bank !!")
pin = 7582
chances = 3
balance = 56000
while chances != 0:
    user_pin = int(input("please enter the four digit pin: "))
    if user_pin != pin :
        chances-= 1
        print("Wrong pin number")
        print(f"you have {chances} chances left")
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw")
        if user_choice == "B" :
            print(f"your total balance is Rs.{balance}")
        if user_choice == "D" :
            deposit_user = int(input("Enter the amount that you would like to deposit"))
            total_balance = deposit_user + balance
            print(f"you have  deposited Rs.{deposit_user}")
            print(f"your total balance is Rs.{total_balance}")
        if user_choice == "W" :
            withdraw_user = int(input("Enter the amount that you want to withdraw"))
            total_balance = balance - withdraw_user
            print(f"you have withdrawn Rs.{total_balance}")
            print(f"your total balance is Rs.{total_balance}")
            user_exit = input("would you like to exit? yes/no")
        if user_exit == "yes":
              print("Thank You for using BBC Bank !!")
              break
        else:
             continue






