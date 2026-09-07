import json
from models.habit import Habit
from pathlib import Path

class JSONStorage:
    def __init__(self, filename):
        data_folder = Path("data")
        data_folder.mkdir(exist_ok=True)

        self.filename = data_folder / filename

    def save(self, habits):

        data = [habit.to_dict() for habit in habits]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        try:
            with open(self.filename) as file:
                data = json.load(file)
            habits = [Habit.from_dict(habit) for habit in data]
            return habits
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("\nHabit data file contains invalid/corrupted JSON.")
            return []