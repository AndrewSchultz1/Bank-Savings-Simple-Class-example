##Andrew Schultz

##Importing class
import savings

##Declaring constants
SAV_RATE = .01
CD_RATE = .015
MAT_DATE= '06/30/2018'

#Declaring main and displaying menu
def main():
  print('Welcome to the Local Community Bank Program')
  print('============================================')

#Getting input from user
  acc_num = input('Please enter the account number: ')
  acc_name = input('Please enter the name on the account: ')
  acc_bal = float(input('Please enter the account balance: '))

#Validation loop
  while acc_bal <= 0:
    print('Account balance is less than or equal to 0')
    acc_bal = float(input('Please enter a valid account balance: '))

#Printing account info and making object
  acc_obj = savings.SavingsAccount(acc_name, acc_bal, acc_num, SAV_RATE)
  print('')
  print("Account information below:")
  print('===========================')
  print(acc_obj)

#Getting input from user
  acc_num = input('Please enter the account number: ')
  acc_name = input('Please enter the name on the account: ')
  acc_bal = float(input('Please enter the account balance: '))

#Validation loop
  while acc_bal <= 0:
    print('Account balance is less than or equal to 0')
    acc_bal = float(input('Please enter a valid account balance: '))

#Making object and printing account info
  CD_obj = savings.CD(acc_name, acc_bal, acc_num, CD_RATE, MAT_DATE)
  print('')
  print("Account information below:")
  print('==========================')
  print(CD_obj)
#Entering loop
  start = input('Would you like to make any transactions? ')
  while start.upper() == 'YES':
#Decision structure for account type
    typeAccount = input('Are you trying to access Savings or CD? ')
    if typeAccount.upper() == 'SAVINGS':
      processAccount(acc_obj)
#Decision structure for account type
    elif typeAccount.upper() == 'CD':
      processAccount(CD_obj)
    else:
#Outputs for the end of the program
      print('Invalid accounttype. ')
    start = input('Would you like to make any transactions? ')
  print('End of Program')
#Display name declaration and print statements
def displayMenu():
  print('Please select from the following choices: ')
  print('')
#More prints
  print('D - Deposit')
  print('W - Withdrawal')
  print('M - Maturity Date')
#More prints and getting choice
  print('P - Print account info')
  choice = input('What do you want to perform? ')
  return choice
#Process amount decleration and receiving choice
def processAccount(account):
  choice = displayMenu()
#deposit for D
  if choice.upper() == 'D':
    amount = int(input('How much would you like to deposit? '))
    savings.SavingsAccount.deposit(account, amount)
    print('Current balance is: ', savings.SavingsAccount.get_bal(account))
#withdrawal for f
  elif choice.upper() =='W':
    amount = int(input('How much would you like to withdrawal? '))
    savings.SavingsAccount.withdrawal(account, amount)
    print('Current balance is: ', savings.SavingsAccount.get_bal(account))
#maturity date for m
  elif choice.upper() == 'M':
    if isinstance( account, savings.CD):
      print('')
#Printing m and rejecting bad account types
      print(savings.CD.get_mat_date(account))
    else:
      print('')
      print('Sorry but that account type does not have a maturity date. ')
#printing for P
  elif choice.upper() == 'P':
    print('')
    print(account)
#Invalid entry printline
  else:
    print('Sorry that entry is invalid')
main()
                     











