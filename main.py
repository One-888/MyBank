import sys


class Account:

    _account_list = []

    def __init__(self, id_number, amount):
        self._id_num = id_number
        self._account_list.append(self)
        self._amount = amount

    # # # @classmethod
    def get_id(self):
        return self._id_num

    # # # @classmethod
    def set_id(self, new_id):
        self._id_num = new_id

    # @property
    def get_amount(self):
        return self._amount

    # @amount.setter
    def set_amount(self, amount):
        self._amount = amount

    def __del__(self):
        return f"   Remove Acct#: {self._id_num} ${self._amount} "

    def __repr__(self):
        return f"   Acct#: {self._id_num} ${self._amount} "


def show_all_accounts(acc_list):
    for i in acc_list:
        print(f"      {i}")
    print("")


def report(acc_list):

    print(f"account;amount")
    for i in acc_list:
        print(f"{i.get_id()};{i.get_amount()}")


def save_file(acc_list):
    x = ""
    for i in acc_list:
        x = x + (f"{i.get_id()};{i.get_amount()}\n")
    return x


def create_account(account_number, amount):

    new_account = Account(account_number, amount)
    return new_account


def find_account(account_list, find_account_number):

    for i in account_list:
        if getattr(i, "_id_num") == find_account_number:
            print(f"        Found: {find_account_number}")
            return i


def menu_help():
    print(
        """
Welcome to My Bank App
        add  = Add a new account
        show = Display all accounts
          
    """
    )


# for i in range(3):
#     a = Account(10)

# print(Account._account_list)

while True:
    menu_help()
    show_all_accounts(Account._account_list)
    mode = (input("Enter Mode: ")).lower()
    if mode == "exit":
        sys.exit()
        # break
    elif mode == "add":
        value = input("Enter Account# and Value (1 20): ")
        id_num, val = value.split(" ")
        account = create_account(id_num, val)
        show_all_accounts(Account._account_list)

    elif mode == "show":
        # print(Account._account_list)
        show_all_accounts(Account._account_list)

    elif mode == "find":
        find_acct = str(input("Find Account#: "))
        ac = find_account(Account._account_list, find_acct)
        print(ac)

    elif mode == "idx":
        find_acct = str(input("Find Account#: "))
        ac_obj = find_account(Account._account_list, find_acct)
        ix = Account._account_list.index(ac_obj)
        print(Account._account_list[ix])

    elif mode == "del":
        find_acct = str(input("Find Account#: "))
        ac_obj = find_account(Account._account_list, find_acct)
        Account._account_list.remove(ac_obj)

    elif mode == "print":
        print("_" * 50)
        report(Account._account_list)
        print("_" * 50)

    elif mode == "load":
        Account._account_list.clear()
        with open("accounts.csv", "r") as f:
            for x in f:
                x = x.strip()
                id_num, val = x.split(";")
                account = create_account(id_num, val)

    elif mode == "save":
        with open("accounts.csv", "w") as f:
            csv = save_file(Account._account_list)
            f.write(csv)

    else:
        print("ERROR: no command")
