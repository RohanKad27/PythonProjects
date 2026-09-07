from managers.habit_tracker import HabitTracker
from utils import display, validators

if __name__ == "__main__":

    tracker = HabitTracker()

    while True:

        display.print_header("HABIT TRACKER")

        print("1. Create Habit")
        print("2. Show Habit")
        print("3. Complete Habit")
        print("4. Remove Habit")
        print("5. Monthly Calendar")
        print("6. Habit Report")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        match choice:
            case 1:
                habit = input("Enter the habit: ").strip()

                if habit == "":
                    print("Habit name cannot be empty.")
                    continue

                tracker.create_habit(habit)

            case 2:
                tracker.show_habits()

            case 3:
                if not tracker.habits:
                    print("No habits found.")
                    continue

                tracker.show_habits()

                habit_number = validators.validate_habit_number(
                    input("\nEnter habit number: "),
                    tracker.habits
                )

                if habit_number is None:
                    print("Invalid habit number.")
                    continue

                tracker.complete_habit(habit_number)

            case 4:
                if not tracker.habits:
                    print("No habits found.")
                    continue

                tracker.show_habits()

                habit_number = validators.validate_habit_number(
                    input("\nEnter habit number: "),
                    tracker.habits
                )

                if habit_number is None:
                    print("Invalid habit number.")
                    continue

                tracker.remove_habit(habit_number)

            case 5:
                if not tracker.habits:
                    print("No habits found.")
                    continue

                tracker.show_habits()

                habit_number = validators.validate_habit_number(
                    input("\nEnter habit number: "),
                    tracker.habits
                )

                if habit_number is None:
                    print("Invalid habit number.")
                    continue

                print("\n1. Previous Month")
                print("2. Current Month")
                print("3. Next Month")

                try:
                    selection = int(input("Select a month to view (1-3): "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if not 1 <= selection <= 3:
                    print("Please enter number between 1 and 3.")
                    continue

                if selection == 1:
                    month_offset = -1
                elif selection == 2:
                    month_offset = 0
                else:
                    month_offset = 1

                tracker.monthly_calendar(habit_number, month_offset)

            case 6:
                tracker.stats_obj.generate_report()

            case 7:
                print("Exiting...")
                break

            case _:
                print("Invalid choice")
