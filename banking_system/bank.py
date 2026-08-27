import csv

def generate_account_no():
    with open("data.csv") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        account_numbers = [int(row[0]) for row in reader]

        if not account_numbers:
            return 1000

        return max(account_numbers)

def create_account():

    account_no = 0

    name = input("Enter name: ")
    try:
        initial_amount = int(input("Enter initial deposit: "))
        if initial_amount < 0:
            print("\nPlease enter a valid amount.")
            return
    except ValueError:
        print("\nPlease enter a valid number.")
        return

    with open("data.csv", "a", newline='') as file:

        account_no = generate_account_no()
        account_no += 1
        writer = csv.writer(file)
        writer.writerow([account_no, name, initial_amount])

    print("\nAccount Created Successfully.")
    print("Account number: ", account_no)


def view_account():
    try:
        account_no = int(input("Enter account number: "))
    except ValueError:
        print("\nPlease enter a valid number.")
        return

    with open("data.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if account_no == int(line[0]):
                print()
                print("="*30)
                print("Account number:", line[0])
                print("Name:", line[1])
                print("Balance:", line[2])
                print("="*30)
                break
        else:
            print("\nAccount not found.")


def deposit():
    try:
        account_no = int(input("Enter account number: "))
        deposit_amount = int(input("Enter amount to deposit: "))
        if deposit_amount < 1:
            print("\nPlease enter a valid amount to deposit.")
            return
    except ValueError:
        print("\nPlease enter a valid number.")
        return

    with open("data.csv") as file:
        reader = csv.reader(file)
        header = next(reader)
        content = list(reader)

    for line in content:
        if account_no == int(line[0]):
            line[2] = str(int(line[2]) + deposit_amount)
            break
    else:
        print("\nAccount not found.")
        return

    with open("data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(content)

    print("\nAmount Deposited Successfully.")

def withdraw():
    try:
        account_no = int(input("Enter account number: "))
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount < 1:
            print("\nPlease enter a valid amount to withdraw.")
            return
    except ValueError:
        print("\nPlease enter a valid number.")
        return

    with open("data.csv") as file:
        reader = csv.reader(file)
        header = next(reader)
        content = list(reader)

    for line in content:
        if account_no == int(line[0]):
            if withdraw_amount > int(line[2]):
                print("\nInsufficient Balance.")
                return

            line[2] = str(int(line[2]) - withdraw_amount)
            break
    else:
        print("\nAccount not found.")
        return

    with open("data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(content)

    print("\nAmount Withdrawn Successfully.")

def check_balance():
    try:
        account_no = int(input("Enter account number: "))
    except ValueError:
        print("\nPlease enter a valid number.")
        return

    with open("data.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if account_no == int(line[0]):
                print()
                print("=" * 30)
                print("Name:", line[1])
                print("Balance:", line[2])
                print("=" * 30)
                break
        else:
            print("\nAccount not found.")

def view_all_accounts():
    with open("data.csv") as file:
        reader = csv.reader(file)
        content = list(reader)

        if len(content) == 1:
            print("\nNo accounts found.")
            return

        print()
        print("=" * 65)
        print("                         All Accounts")
        print("=" * 65)

        print(f"{content[0][0]:<20} {content[0][1]:<20} {content[0][2]:<30}")
        print("-" * 65)

        for line in content[1:]:
            print(f"{line[0]:<20} {line[1]:<20} {line[2]:<30}")


if __name__ == '__main__':

    choice = 0

    with open("data.csv", "a+", newline='') as File:

        File.seek(0)
        reader = csv.reader(File)

        if not list(reader):
            writer = csv.writer(File)
            writer.writerow(["account_no", "name", "balance"])

    print()
    print("="*30)
    print("    PYTHON BANKING SYSTEM")
    print("=" * 30)

    while choice != 7:
        print("\nMenu")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. View All Accounts")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        match choice:
            case 1:
                create_account()
            case 2:
                view_account()
            case 3:
                deposit()
            case 4:
                withdraw()
            case 5:
                check_balance()
            case 6:
                view_all_accounts()
            case 7:
                print("Exiting....")
                break
            case default:
                print("Invalid choice.")