from models.habit import Habit
from storage.json_storage import JSONStorage
from reports.stats import Stats
import calendar
from datetime import date, datetime
from utils import display


class HabitTracker:
    def __init__(self):
        self.storage = JSONStorage("habits.json")
        self.habits = self.storage.load()
        self.stats_obj = Stats(self.habits)

    def create_habit(self, name):
        habit = Habit(name)
        self.habits.append(habit)
        self.storage.save(self.habits)

    def get_habit_by_number(self, number):
        if 1 <= number <= len(self.habits):
            return self.habits[number - 1]

        return None

    def complete_habit(self, habit_number):
        habit = self.get_habit_by_number(habit_number)

        if habit is None:
            print("Habit not found.")
            return

        habit.complete()
        self.storage.save(self.habits)

    def remove_habit(self, habit_number):
        habit = self.get_habit_by_number(habit_number)

        if habit is None:
            print("Habit not found.")
            return

        self.habits.remove(habit)
        self.storage.save(self.habits)

    def show_habits(self):
        if self.habits:

            display.print_header("YOUR HABITS")

            for number, habit in enumerate(self.habits, start=1):
                print(f"Habit No. {number}")
                habit.show()
                percentage = self.stats_obj.completion_percentage(habit.id)
                print(f"Completion percentage: {percentage:.2f}%")
                print("-" * 50)

            # print(f"Average completions per habit: {self.stats_obj.average_completions()}")
            # print(f"Most consistent habit: {self.stats_obj.highest_completion_habit()}")
            # print(f"Longest streak: {self.stats_obj.longest_streak()}")
        else:
            print("No habits found.")

    def monthly_calendar(self, habit_number, month_offset=0):

        today = datetime.now().date()
        year = today.year
        month = today.month

        # Month offset calculation
        total_months = year * 12 + (month - 1)
        total_months += month_offset
        year = total_months // 12
        month = total_months % 12 + 1

        month_calendar = calendar.monthcalendar(year, month)

        selected_habit = self.get_habit_by_number(habit_number)

        if selected_habit is None:
            print("Habit not found.")
            return

        print()
        #year and month printing
        display.print_header(
            f"{selected_habit.name} - {calendar.month_name[month]} {year}"
        )

        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for day_name in weekdays:
            print(f"{day_name:^8}", end="")

        print()

        for week in month_calendar:
            for day in week:
                if day == 0:
                    print(" " * 8, end="")
                    continue

                day_obj = date(year, month, day)

                if day_obj in selected_habit.completed_dates:
                    symbol = "✅"
                else:
                    symbol = "❌"

                print(f"{day:2} {symbol:^4}", end="")
            print()

        print()
        print("Legend:  ✅ Completed    ❌ Not completed")