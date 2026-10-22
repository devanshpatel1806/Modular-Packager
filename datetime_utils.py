
# DATETIME AND TIME UTILITIES

import datetime
import time

# CURRENT DATE AND TIME

def show_current_datetime():
    """Display the current date and time."""

    current = datetime.datetime.now()

    print("\nCurrent Date and Time:")
    print(current.strftime("%Y-%m-%d %H:%M:%S"))


# DATE DIFFERENCE


def calculate_date_difference():
    """Calculate difference between two dates."""

    try:
        first_date = input(
            "\nEnter the first date (YYYY-MM-DD): "
        )

        second_date = input(
            "Enter the second date (YYYY-MM-DD): "
        )

        date1 = datetime.datetime.strptime(
            first_date, "%Y-%m-%d"
        )

        date2 = datetime.datetime.strptime(
            second_date, "%Y-%m-%d"
        )

        difference = abs((date2 - date1).days)

        print(f"\nDifference: {difference} days")

    except ValueError:
        print("\nInvalid date format.")
        print("Please use YYYY-MM-DD.")

# CUSTOM DATE FORMAT


def format_date():
    """Display the current date in different formats."""

    current = datetime.datetime.now()

    print("\nAvailable Date Formats:")
    print("1. DD-MM-YYYY")
    print("2. DD/MM/YYYY")
    print("3. Month Day, Year")
    print("4. Day, Month Day Year")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(
            "Formatted Date:",
            current.strftime("%d-%m-%Y")
        )

    elif choice == "2":
        print(
            "Formatted Date:",
            current.strftime("%d/%m/%Y")
        )

    elif choice == "3":
        print(
            "Formatted Date:",
            current.strftime("%B %d, %Y")
        )

    elif choice == "4":
        print(
            "Formatted Date:",
            current.strftime("%A, %B %d %Y")
        )

    else:
        print("Invalid choice.")


# STOPWATCH

def stopwatch():
    """Run a simple stopwatch."""

    print("\nSTOPWATCH")
    print("Press ENTER to start.")

    input()

    start_time = time.time()

    print("Stopwatch started.")
    print("Press ENTER to stop.")

    input()

    end_time = time.time()

    elapsed = end_time - start_time

    print(f"\nElapsed Time: {elapsed:.2f} seconds")


# COUNTDOWN TIMER

def countdown_timer():
    """Run a simple countdown timer."""

    try:
        seconds = int(
            input("\nEnter countdown time in seconds: ")
        )

        if seconds <= 0:
            print("Please enter a positive number.")
            return

        print("\nCountdown started...")

        for remaining in range(seconds, 0, -1):
            print(
                f"Remaining: {remaining} seconds",
                end="\r"
            )

            time.sleep(1)

        print("\nTime's up!")

    except ValueError:
        print("Please enter a valid number.")


# DATETIME MENU

def datetime_menu():
    """Display datetime and time operations."""

    while True:

        print("\n" + "=" * 45)
        print("       DATETIME AND TIME OPERATIONS")
        print("=" * 45)

        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Dates")
        print("3. Format Date into Custom Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            show_current_datetime()

        elif choice == "2":
            calculate_date_difference()

        elif choice == "3":
            format_date()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


# MAIN CHECK

if __name__ == "__main__":
    datetime_menu()