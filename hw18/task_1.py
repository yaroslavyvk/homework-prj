import unittest
from unittest.mock import patch
from io import StringIO


class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self._interest = interest

    def add_interest(self):
        self._balance += self._balance * self._interest

    def __str__(self):
        return super().__str__() + f', interest: {self._interest}'


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        else:
            super().withdraw(amount)

    def is_overdrawn(self):
        return self._balance < 0

    def __str__(self):
        return super().__str__() + f', overdraft limit: {self._overdraft_limit}'


class Bank:
    def __init__(self):
        self._accounts = []

    def get_accounts(self):
        return self._accounts

    def open_account(self, account_type, account_number, **kwargs):

        if account_type == "savings":
            interest = kwargs.get('interest', 0.0)
            account = SavingsAccount(0.0, account_number, interest)

        elif account_type == "current":
            overdraft_limit = kwargs.get('overdraft_limit', 0.0)
            account = CurrentAccount(0.0, account_number, overdraft_limit)

        else:
            raise ValueError(f"Invalid account type: {account_type}")

        self._accounts.append(account)

    def close_account(self, account_number):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                self._accounts.remove(account)
                break

    def pay_dividend(self, dividend_amount):
        for account in self._accounts:
            account.deposit(dividend_amount)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                print(f"Letter sent to account {account.get_account_number()} due to overdraft")


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account_savings(self):
        self.bank.open_account("savings", "001", interest=0.05)
        accounts = self.bank.get_accounts()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].get_balance(), 0.0)
        self.assertEqual(accounts[0].get_account_number(), "001")
        self.assertTrue(isinstance(accounts[0], SavingsAccount))

    def test_open_account_current(self):
        self.bank.open_account("current", "002", overdraft_limit=1000)
        accounts = self.bank.get_accounts()
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].get_balance(), 0.0)
        self.assertEqual(accounts[0].get_account_number(), "002")
        self.assertTrue(isinstance(accounts[0], CurrentAccount))

    def test_open_account_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.bank.open_account("invalid", "003")
        self.assertEqual(str(context.exception), "Invalid account type: invalid")

    @patch("sys.stdout", new_callable=StringIO)
    def test_update_interest_and_overdraft(self, mock_stdout):
        self.bank.open_account("savings", "001", interest=0.05)
        self.bank.open_account("current", "002", overdraft_limit=1000)
        current_account = self.bank.get_accounts()[1]
        current_account.withdraw(950)
        self.bank.update()

        self.assertEqual(self.bank.get_accounts()[0].get_balance(), 0.0)
        self.assertEqual(self.bank.get_accounts()[1].get_balance(), -950)
        self.assertIn("Letter sent to account 002 due to overdraft", mock_stdout.getvalue())


unittest.main()
