def reverse_string(s: str) -> str:
    return s[::-1]


print(reverse_string("hello"))


def squares_of_even_numbers(numbers: list) -> list:
    return [x ** 2 for x in numbers if x % 2 == 0]


print(squares_of_even_numbers([1, 2, 3, 4, 5])) 


def count_words_in_file(filename: str) -> int:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)


print(count_words_in_file('example.txt'))


def sort_dict_by_values(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1]))


example_dict = {'a': 3, 'b': 1, 'c': 2}
print(sort_dict_by_values(example_dict))  # Output: {'b': 1, 'c': 2, 'a': 3}


def read_accounts():
    accounts = {}
    with open('accounts.txt', 'r') as file:
        for line in file:
            account_number, balance = line.strip().split(',')
            accounts[account_number] = float(balance)
    return accounts


def write_accounts(accounts):
    with open('accounts.txt', 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f"{account_number},{balance}\n")


def get_balance(account_number):
    accounts = read_accounts()
    return accounts.get(account_number, 0.0)


def deposit(account_number, amount):
    accounts = read_accounts()
    if account_number in accounts:
        accounts[account_number] += amount
        write_accounts(accounts)
    else:
        print(f"Account {account_number} does not exist.")


def withdraw(account_number, amount):
    accounts = read_accounts()
    if account_number in accounts:
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            write_accounts(accounts)
        else:
            print("Insufficient balance.")
    else:
        print(f"Account {account_number} does not exist.")


def update_account(account_number, balance):
    accounts = read_accounts()
    if account_number in accounts:
        accounts[account_number] = balance
        write_accounts(accounts)
    else:
        print(f"Account {account_number} does not exist.")


def test_bank_account_management():
    initial_data = """12345,1000.0
67890,500.0
11121,1500.0"""

    with open('accounts.txt', 'w') as file:
        file.write(initial_data)

    print(get_balance("12345"))  # Output: 1000.0
    print(get_balance("67890"))  # Output: 500.0
    print(get_balance("11121"))  # Output: 1500.0
    print(get_balance("00000"))  # Output: 0.0 (non-existent account)

    deposit("12345", 200.0)
    print(get_balance("12345"))  # Output: 1200.0

    withdraw("67890", 100.0)
    print(get_balance("67890"))  # Output: 400.0
    withdraw("67890", 1000.0)  # Output: Insufficient balance.

    update_account("11121", 2000.0)
    print(get_balance("11121"))  # Output: 2000.0

    deposit("00000", 100.0)  # Output: Account 00000 does not exist.
    withdraw("00000", 50.0)  # Output: Account 00000 does not exist.
    update_account("00000", 300.0)  # Output: Account 00000 does not exist.


test_bank_account_management()
