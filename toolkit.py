# toolkit.py
# Python Multi-Tool Utility Program
# Features a main menu loop, error handling for invalid choices, and three interactive tools.

import random


# Tool 1: Number Guessing Game
def number_guessing_game():
    """Allows the user to guess a randomly generated number between 1 and 10 with feedback."""
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0

    print("I have picked a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess (or 0 to exit to menu): "))
            if guess == 0:
                print("Returning to main menu...")
                break

            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")


# Tool 2: Quick To-Do List Manager
def todo_manager():
    """Manages a dynamic task list where users can add and view tasks."""
    print("\n--- Quick To-Do List Manager ---")
    tasks = []

    while True:
        print("\nTo-Do Menu: [1] View Tasks  [2] Add Task  [3] Clear List  [4] Back to Main Menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' added successfully!")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            tasks.clear()
            print("All tasks have been cleared.")
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option! Please choose between 1 and 4.")


# Tool 3: Tip Calculator
def tip_calculator():
    """Calculates tip and total bill based on bill amount and service rating."""
    print("\n--- Tip Calculator ---")
    try:
        bill_amount = float(input("Enter the total bill amount ($): "))
        if bill_amount < 0:
            print("Bill amount cannot be negative.")
            return

        print("Service Rating: [1] Good (20%)  [2] Fair (15%)  [3] Poor (10%)")
        rating = input("Choose service rating (1-3): ").strip()

        if rating == "1":
            tip_percent = 0.20
        elif rating == "2":
            tip_percent = 0.15
        elif rating == "3":
            tip_percent = 0.10
        else:
            print("Invalid rating chosen. Defaulting to 15%.")
            tip_percent = 0.15

        tip_amount = bill_amount * tip_percent
        total_bill = bill_amount + tip_amount

        print("\n--- Calculation Summary ---")
        print(f"Bill Amount: ${bill_amount:.2f}")
        print(f"Tip Amount:  ${tip_amount:.2f}")
        print(f"Total Due:   ${total_bill:.2f}")
        print("---------------------------")

    except ValueError:
        print("Invalid number entered. Please enter valid numeric values.")


# Main Program Loop
def main():
    print("========================================")
    print("   WELCOME TO PYTHON TOOLKIT")
    print("========================================")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Number Guessing Game")
        print("2. Quick To-Do List Manager")
        print("3. Tip Calculator")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_manager()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("\nThank you for using Python Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
