class BankAccount:
    def __init__(self, owner_name, account_number, balance, password):
        self.owner_name = owner_name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Incorrect password. Try again."

    def set_balance(self, new_balance, password):
        if password == self.__password:
            self.__balance = new_balance
            return "Balance updated. Have a nice day!"
        else:
            return "Incorrect password. Try again"
