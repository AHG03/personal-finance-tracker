class Transaction():
    def __init__(self, amount, kind, category, note):
        self.amount = amount
        self.kind = kind
        self.category = category
        self.note = note


class FinanceManager():
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, kind, category, note):
        transaction = Transaction(amount, kind, category, note)
        self.transactions.append(transaction)


    def show_transactions(self):
        for transaction in self.transactions:
            print(f"Amount: {transaction.amount}, kind: {transaction.kind}, Category: {transaction.category}, Note: {transaction.note}")


def main():
    finance_manager = FinanceManager()
    while True:
        print("\nWelcome to my personal finance tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Exit")

        choice = input("Please enter your choice: ")
        if choice == "1":
            amount = float(input("Please enter the amount: $"))
            kind = input("Please enter the transaction kind (income/expense):")
            category = input("Please enter the transaction category: ")
            note = input("Please enter the transaction note: ")

            finance_manager.add_transaction(amount, kind, category, note)

        elif choice == "2":
            finance_manager.show_transactions()

        elif choice == "3":
            break


if __name__ == "__main__":
    main()