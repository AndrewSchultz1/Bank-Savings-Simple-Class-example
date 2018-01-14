import math

class SavingsAccount:

  def __init__(self, name, bal, account_num, int_rate):
    self.__name = name
    self.__bal = bal
    self.__account_num = account_num
    self.__int_rate = int_rate

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_account_num(self):
    return self.__account_num

  def set_account_num(self, acount_num):
    self.__account_num = account_num

  def get_int_rate(self):
    return self.__int_rate

  def set_name(self, int_rate):
    self.__int_rate = int_rate

  def get_bal(self):
    return self.__bal

  def set_bal(self, bal):
    self.__bal = bal

  def deposit(self, amount):
    if amount > 0:
      self.__bal += amount
    else:
      print('''We're sorry, that's not a valid amount. ''')

  def withdrawal(self, amount):
    if amount <= 0:
      print("Sorry but you can't withdrawal negative or zero dollars from an account.")
    elif self.__bal - amount < 10:
      print('Your balance is: ', self.__bal)
      print("The limit for your withdrawal is: ", self.__bal - 10)
    else:
      self.__bal -= amount

  def __str__(self):
    return "The account number is " + str(self.__account_num) + "\n" + "The name is " + str(self.__name) + "\n" + "The balance is: " + str(self.__bal) + "\n" + "The interest rate is " + str(self.__int_rate) + "\n" 


class CD(SavingsAccount):

  def __init__ (self, name, bal, account_num, int_rate, mat_date):
    SavingsAccount.__init__(self, name, bal, account_num, int_rate)
    self.__mat_date = mat_date

  def set_mat_date(self, mat_date):
    self.__mat_date = mat_date

  def get_mat_date(self):
    return self.__mat_date

  def __str__(self):
    return  SavingsAccount.__str__(self) + "The maturity date is " + str(self.__mat_date) + "\n"

