class BankAccount:
	__no_of_accounts = 0
	def __init__(self, n, b=0):
		"""name -- must be in name
		balance -- must be in balance"""
		self.__name = n
		self.__balance = b
		if b < 0:
			b = 0
		BankAccount.__no_of_accounts += 1
		print("A bank account for " + n +" is open.")
		print("Your current balance is " + str(b) + " won.")

	@staticmethod
	def count_accounts():
		"""return no_of_accounts"""
		return BankAccount.__no_of_accounts

	def __str__(self):
		"""return its string representation"""
		return self.__name + "'s BankAccount object."

	def show_balance(self):
		"""show balance"""
		print(self.__name + "'s balance is " + str(self.__balance) + " won.")

	def deposit(self,amount):
		"""deposit amount"""
		if amount >= 0:
			self.__balance += amount
			print(str(amount) + " won has been successfully deposited.")
			# print(self.__name + "'s balance is " + str(self.__balance) + " won.")
			self.show_balance()
		else:
			print("Deposit failed.")
			# print(self.__name + "'s balance is " + str(self.__balance) + " won.")
			self.show_balance()
	def withdraw(self,amount):
		"""withdraw amount"""
		if amount >= 0 and self.__balance - amount >= 0:
			self.__balance -= amount
			print(str(amount) + " won has been successfully withdrawn.")
			# print(self.__name + "'s balance is " + str(self.__balance) + " won.")
			self.show_balance()
		else:
			print("Withdraw failed")
			# print(self.__name + "'s balance is " + str(self.__balance) + " won.")
			self.show_balance()


