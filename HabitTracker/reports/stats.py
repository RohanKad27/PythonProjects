import statistics
from datetime import datetime
from utils import display


class Stats:
    def __init__(self, habits):
        self.habits = habits

    def average_completions(self):
        try:
            counts = [habit.completion_count() for habit in self.habits]
            average_completion = statistics.mean(counts)
            return average_completion
        except statistics.StatisticsError:
            return 0.0

    def highest_completion_habit(self):
        completions = {habit.name:habit.completion_count() for habit in self.habits}

        if not completions:
            return "Currently no habits exist."

        completions = sorted(completions.items(), key=lambda x: x[1], reverse=True)

        if completions[0][1] == 0:
            return "Currently no habits are completed."

        return completions[0][0]

    def completion_percentage(self, habit_id):

        today = datetime.now()

        for habit in self.habits:
            if habit.id == habit_id:
                selected_habit = habit
                break
        else:
            print("Habit not found.")
            return

        possible_days = abs(today.date() - selected_habit.created_at.date()).days + 1
        completed_days = selected_habit.completion_count()
        percentage = (completed_days / possible_days) * 100

        return percentage

    def longest_streak(self):
        streak_list = [habit.longest_streak() for habit in self.habits]

        if not streak_list:
            return 0

        return max(streak_list)

    def generate_report(self):
        display.print_header("HABITS REPORT")

        print(f"Total habits          : {len(self.habits)}")
        print(f"Average completions   : {self.average_completions():.2f}")
        print(f"Most completed habit  : {self.highest_completion_habit()}")
        print(f"Longest streak        : {self.longest_streak()} days")
