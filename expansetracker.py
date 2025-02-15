functions and overall program structure index. Please enter a valid expense number.")
        except ValueError:
            print("Please enter a numeric index.")
    
    def run(self):
        """Main loop for user interaction."""
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Analyze Expenses")
            print("4. Delete Expense")
            print("5. Exit")
            choice = input("Select an option: ")
            
            if choice == "1":
                amount = input("Enter amount: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                date = input("Enter date (YYYY-MM-DD HH:MM:SS) or leave blank for current time: ")
                self.add_expense(amount, category, description, date)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.analyze_expenses()
            elif choice == "4":
                self.view_expenses()
                index = input("Enter the expense number to delete: ")
                self.delete_expense(index)
            elif choice == "5":
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__expansetracker__":
    tracker = ExpenseTracker()
    tracker.run()
