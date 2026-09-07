import uuid
from datetime import datetime, date, timedelta

class Habit:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.name = name
        self.completed_dates = set()

    def complete(self):
        today = datetime.now().date()

        if today in self.completed_dates:
            print("Habit already completed today.")
        else:
            self.completed_dates.add(today)

    def show(self):

        today = datetime.now().date()

        time_elapsed = self.age()
        hours = time_elapsed.seconds // 3600
        remaining_seconds = time_elapsed.seconds % 3600
        minutes = remaining_seconds // 60

        day_word = "day" if time_elapsed.days == 1 else "days"
        hour_word = "hour" if hours == 1 else "hours"
        minute_word = "minute" if minutes == 1 else "minutes"

        streak = self.streak()
        longest = self.longest_streak()
        streak_word = "day" if streak == 1 else "days"
        longest_word = "day" if longest == 1 else "days"

        status = '✅' if today in self.completed_dates else '❌'

        total_completions = self.completion_count()

        print("-" * 50)
        print(f"Habit          : {self.name}")
        # print(f"ID             : {self.id}")
        print(f"Status         : {status}")
        print(f"Created        : {self.created_at.strftime('%d-%b-%Y, %H:%M')}")
        print(f"Habit age      : {time_elapsed.days} {day_word}, {hours} {hour_word}, {minutes} {minute_word}")
        print(f"Current streak : {streak} {streak_word}")
        print(f"Longest streak : {longest} {longest_word}")
        print(f"Completions    : {total_completions}")
        print("-" * 50)


    def age(self):
        current_time = datetime.now()
        difference = current_time - self.created_at
        return difference

    def streak(self):
        today = datetime.now().date()
        streak = 0

        for i in range(0, len(self.completed_dates)):
            check_date = today - timedelta(days = i)
            if check_date in self.completed_dates:
                streak += 1
            else:
                break

        return streak

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "completed_dates": [completed_date.isoformat() for completed_date in self.completed_dates]
        }

        return data

    @classmethod
    def from_dict(cls, data):
        habit = cls(data["name"])

        habit.id = data["id"]
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.completed_dates = {date.fromisoformat(completed_date) for completed_date in data["completed_dates"]}

        return habit

    def completion_count(self):
        return len(self.completed_dates)

    def longest_streak(self):
        dates = sorted(self.completed_dates)

        if not dates:
            return 0

        streak = 1
        maximum = 1

        for i in range(1, len(dates)):
            # compare dates[i] with dates[i - 1]
            if (dates[i] - dates[i-1]) == timedelta(days=1):
                    streak += 1
            else:
                if streak > maximum:
                    maximum = streak
                streak = 1

            if streak > maximum:
                maximum = streak

        return maximum