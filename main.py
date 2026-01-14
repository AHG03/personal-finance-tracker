import json


class Transaction:
    def __init__(self, amount, transaction_type, category, note):
        self.amount = amount
        self.transaction_type = transaction_type
        self.category = category
        self.note = note


class FinanceManager:
    def __init__(self):
        self.transactions = []


    def add_transaction(self, amount, transaction_type, category, note):
        transaction = Transaction(amount, transaction_type, category, note)
        self.transactions.append(transaction)


    def show_transactions(self):
        for transaction in self.transactions:
            print(f"Amount: {transaction.amount}, transaction_type: {transaction.transaction_type}, Category: {transaction.category}, Note: {transaction.note}")


    def load_from_file(self):
        try:
            with open("transactions.json", 'r') as file:
                data = json.load(file)
                self.transactions = []
                for item in data:
                    transaction = Transaction(item["amount"], item["transaction_type"], item["category"], item["note"])
                    self.transactions.append(transaction)
        except FileNotFoundError:
            with open("transactions.json", 'w') as file:
                json.dump([], file)


    def save_to_file(self):
        data = []
        for item in self.transactions:
            data.append({"amount": item.amount, "transaction_type": item.transaction_type, "category": item.category, "note": item.note})
        with open("transactions.json", 'w') as file:
            json.dump(data, file, indent=4)


def main():
    finance_manager = FinanceManager()
    finance_manager.load_from_file()

    while True:
        print("\nWelcome to my personal finance tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Exit")

        choice = input("Please enter your choice: ")
        if choice == "1":
            amount = float(input("Please enter the amount: $"))
            transaction_type = input("Please enter the transaction type (income/expense): ")
            category = input("Please enter the transaction category: ")
            note = input("Please enter the transaction note: ")

            finance_manager.add_transaction(amount, transaction_type, category, note)
            finance_manager.save_to_file()

        elif choice == "2":
            finance_manager.show_transactions()

        elif choice == "3":
            break


if __name__ == "__main__":
    main()